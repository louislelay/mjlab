"""Goal-reaching command term.

Samples goal positions (x, y) and target headings in the world frame.
The command output is the relative goal in the robot body frame plus
heading error: [dx_b, dy_b, dθ].

Supports two goal sampling strategies:
  - flat_patch: Sample from precomputed flat patch positions on the terrain.
    Guarantees goals land on walkable surfaces. Requires terrain with
    FlatPatchSamplingCfg enabled.
  - ring: Uniform sampling in a ring around the robot (original fallback).

Inspired by AME-2 (Zhang et al., 2025) goal-reaching formulation with
optional distance clipping for infinite-horizon deployment.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Literal

import numpy as np
import torch

from mjlab.entity import Entity
from mjlab.managers.command_manager import CommandTerm, CommandTermCfg
from mjlab.utils.lab_api.math import (
  matrix_from_quat,
  quat_apply_inverse,
  wrap_to_pi,
)

if TYPE_CHECKING:
  from mjlab.envs.manager_based_rl_env import ManagerBasedRlEnv
  from mjlab.viewer.debug_visualizer import DebugVisualizer


class GoalPositionCommand(CommandTerm):
  """Samples a goal (x, y, heading) and outputs body-frame relative command.

  Command vector layout: [dx_b, dy_b, dθ]
    - dx_b, dy_b: goal position relative to robot in body frame (meters).
    - dθ: heading error wrapped to [-π, π] (radians).

  When ``sampling_strategy="flat_patch"``, goals are sampled from precomputed
  flat patches on the terrain. This guarantees goals are on walkable surfaces
  (not inside walls, over gaps, or off cliffs). Falls back to ring sampling
  if the terrain has no flat patches or none are within the distance range.
  """

  cfg: GoalPositionCommandCfg

  def __init__(self, cfg: GoalPositionCommandCfg, env: ManagerBasedRlEnv):
    super().__init__(cfg, env)
    self.robot: Entity = env.scene[cfg.entity_name]

    # Command buffer: [dx_b, dy_b, dθ].
    self.goal_command_b = torch.zeros(self.num_envs, 3, device=self.device)

    # World-frame goal storage.
    self.goal_pos_w = torch.zeros(self.num_envs, 2, device=self.device)
    self.goal_heading_w = torch.zeros(self.num_envs, device=self.device)

    # Distance to goal (for curriculum / logging).
    self.goal_distance = torch.zeros(self.num_envs, device=self.device)

    # Resolve flat patch tensor from terrain if available.
    # Shape: (num_rows, num_cols, num_patches, 3)
    self._flat_patches: torch.Tensor | None = None
    self._terrain = env.scene.terrain
    if (
      cfg.sampling_strategy == "flat_patch"
      and self._terrain is not None
      and hasattr(self._terrain, "flat_patches")
    ):
      patches = self._terrain.flat_patches.get(cfg.flat_patch_key)
      if patches is not None:
        self._flat_patches = patches
      else:
        available = list(self._terrain.flat_patches.keys())
        print(
          f"[GoalPositionCommand] WARNING: flat_patch_key='{cfg.flat_patch_key}' "
          f"not found in terrain. Available: {available}. Falling back to ring sampling."
        )

    self.metrics["error_pos_xy"] = torch.zeros(self.num_envs, device=self.device)
    self.metrics["error_heading"] = torch.zeros(self.num_envs, device=self.device)

  @property
  def command(self) -> torch.Tensor:
    return self.goal_command_b

  def _update_metrics(self) -> None:
    max_command_time = self.cfg.resampling_time_range[1]
    max_command_step = max_command_time / self._env.step_dt
    self.metrics["error_pos_xy"] += self.goal_distance / max_command_step
    heading_error = wrap_to_pi(self.goal_heading_w - self.robot.data.heading_w)
    self.metrics["error_heading"] += torch.abs(heading_error) / max_command_step

  def _resample_command(self, env_ids: torch.Tensor) -> None:
    if self._flat_patches is not None:
      self._resample_from_flat_patches(env_ids)
    else:
      self._resample_from_ring(env_ids)

  def _resample_from_flat_patches(self, env_ids: torch.Tensor) -> None:
    """Sample goal positions from precomputed flat patches on the terrain.

    For each env, picks a random flat patch from its assigned sub-terrain,
    filtered by distance range. Falls back to ring sampling per-env if no
    valid patches exist within range.
    """
    assert self._flat_patches is not None
    assert self._terrain is not None
    n = len(env_ids)

    # Get terrain assignments for these envs.
    terrain_levels = self._terrain.terrain_levels[env_ids]  # [n]
    terrain_types = self._terrain.terrain_types[env_ids]  # [n]

    # Gather flat patches for each env's sub-terrain: [n, num_patches, 3]
    patches = self._flat_patches[terrain_levels, terrain_types]  # [n, P, 3]

    robot_xy = self.robot.data.root_link_pos_w[env_ids, :2]  # [n, 2]

    # Compute distance from robot to each patch.
    patch_xy = patches[:, :, :2]  # [n, P, 2]
    delta = patch_xy - robot_xy.unsqueeze(1)  # [n, P, 2]
    dists = torch.norm(delta, dim=2)  # [n, P]

    # Filter patches by distance range.
    dist_min, dist_max = self.cfg.ranges.goal_dist
    valid = (dists >= dist_min) & (dists <= dist_max)  # [n, P]

    # Uniform sampling over valid patches via Gumbel-max trick.
    log_weights = torch.zeros_like(dists)
    log_weights[~valid] = -float("inf")
    gumbel_noise = -torch.log(-torch.log(torch.rand_like(log_weights).clamp(min=1e-8)))
    scores = log_weights + gumbel_noise  # [n, P]
    selected_idx = scores.argmax(dim=1)  # [n]

    # Check which envs had at least one valid patch.
    has_valid = valid.any(dim=1)  # [n]

    # Gather selected patch positions.
    selected_patches = patches[
      torch.arange(n, device=self.device), selected_idx
    ]  # [n, 3]

    self.goal_pos_w[env_ids[has_valid], 0] = selected_patches[has_valid, 0]
    self.goal_pos_w[env_ids[has_valid], 1] = selected_patches[has_valid, 1]

    # Sample heading for envs with valid patches.
    if has_valid.any():
      valid_env_ids = env_ids[has_valid]
      r = torch.empty(int(has_valid.sum().item()), device=self.device)
      if self.cfg.ranges.heading is not None:
        self.goal_heading_w[valid_env_ids] = r.uniform_(*self.cfg.ranges.heading)
      else:
        goal_delta = self.goal_pos_w[valid_env_ids] - robot_xy[has_valid]
        self.goal_heading_w[valid_env_ids] = torch.atan2(
          goal_delta[:, 1], goal_delta[:, 0]
        )

    # Fall back to ring sampling for envs with no valid patches.
    if (~has_valid).any():
      self._resample_from_ring(env_ids[~has_valid])

  def _resample_from_ring(self, env_ids: torch.Tensor) -> None:
    """Uniform sampling in a ring around the robot (fallback strategy)."""
    n = len(env_ids)
    r = torch.empty(n, device=self.device)

    dist = r.uniform_(self.cfg.ranges.goal_dist[0], self.cfg.ranges.goal_dist[1])
    angle = r.uniform_(-torch.pi, torch.pi)

    robot_xy = self.robot.data.root_link_pos_w[env_ids, :2]
    self.goal_pos_w[env_ids, 0] = robot_xy[:, 0] + dist * torch.cos(angle)
    self.goal_pos_w[env_ids, 1] = robot_xy[:, 1] + dist * torch.sin(angle)

    if self.cfg.ranges.heading is not None:
      self.goal_heading_w[env_ids] = r.uniform_(*self.cfg.ranges.heading)
    else:
      self.goal_heading_w[env_ids] = angle

  def _update_command(self) -> None:
    # World-frame displacement to goal.
    robot_xy = self.robot.data.root_link_pos_w[:, :2]
    delta_w = self.goal_pos_w - robot_xy  # [B, 2]

    self.goal_distance = torch.norm(delta_w, dim=1)

    # Optional distance clipping (AME-2 infinite-horizon style).
    if self.cfg.max_goal_distance is not None:
      scale = torch.clamp(
        self.cfg.max_goal_distance / (self.goal_distance + 1e-6), max=1.0
      )
      delta_w = delta_w * scale.unsqueeze(1)

    # Rotate displacement into body frame.
    delta_w_3d = torch.cat(
      [delta_w, torch.zeros(self.num_envs, 1, device=self.device)], dim=1
    )
    delta_b = quat_apply_inverse(self.robot.data.root_link_quat_w, delta_w_3d)
    self.goal_command_b[:, 0] = delta_b[:, 0]
    self.goal_command_b[:, 1] = delta_b[:, 1]

    # Heading error.
    self.goal_command_b[:, 2] = wrap_to_pi(
      self.goal_heading_w - self.robot.data.heading_w
    )

    # Resample if goal reached.
    if self.cfg.resample_on_reach:
      reached = self.goal_distance < self.cfg.reach_threshold
      reached_ids = reached.nonzero(as_tuple=False).flatten()
      if len(reached_ids) > 0:
        self._resample_command(reached_ids)

  # Visualization.

  def _debug_vis_impl(self, visualizer: "DebugVisualizer") -> None:
    """Draw goal position marker and direction arrow."""
    env_indices = visualizer.get_env_indices(self.num_envs)
    if not env_indices:
      return

    base_pos_ws = self.robot.data.root_link_pos_w.cpu().numpy()
    goal_pos_ws = self.goal_pos_w.cpu().numpy()

    for batch in env_indices:
      base_pos = base_pos_ws[batch]
      goal_pos = goal_pos_ws[batch]

      if np.linalg.norm(base_pos) < 1e-6:
        continue

      # Goal marker (red sphere approximated by arrow to self).
      goal_3d = np.array([goal_pos[0], goal_pos[1], base_pos[2] + 0.5])
      visualizer.add_arrow(
        goal_3d,
        goal_3d + np.array([0, 0, 0.3]),
        color=(0.8, 0.2, 0.2, 0.8),
        width=0.03,
      )

      # Direction arrow from robot to goal (yellow).
      from_pt = np.array([base_pos[0], base_pos[1], base_pos[2] + 0.5])
      to_pt = goal_3d
      visualizer.add_arrow(
        from_pt, to_pt, color=(0.8, 0.8, 0.2, 0.5), width=0.01
      )


@dataclass(kw_only=True)
class GoalPositionCommandCfg(CommandTermCfg):
  """Configuration for goal-reaching command term."""

  entity_name: str

  #: Goal sampling strategy.
  #: "flat_patch": sample from precomputed flat patches (requires terrain config).
  #: "ring": uniform sampling in a ring around the robot.
  sampling_strategy: Literal["flat_patch", "ring"] = "flat_patch"

  #: Key into terrain.flat_patches dict. Must match a FlatPatchSamplingCfg name
  #: in the sub-terrain configs.
  flat_patch_key: str = "goal_targets"

  #: Maximum clipped goal distance fed to the policy (None = no clipping).
  #: AME-2 uses 2.0m for infinite-horizon deployment.
  max_goal_distance: float | None = 2.0

  #: Whether to resample the goal when the robot reaches it.
  resample_on_reach: bool = True

  #: Distance threshold to consider goal reached (meters).
  reach_threshold: float = 0.3

  @dataclass
  class Ranges:
    #: Min and max goal distance from robot (meters).
    goal_dist: tuple[float, float] = (1.0, 5.0)
    #: Target heading range (None = face towards goal).
    heading: tuple[float, float] | None = (-3.14159, 3.14159)

  ranges: Ranges = field(default_factory=Ranges)

  @dataclass
  class VizCfg:
    z_offset: float = 0.5

  viz: VizCfg = field(default_factory=VizCfg)

  def build(self, env: ManagerBasedRlEnv) -> GoalPositionCommand:
    return GoalPositionCommand(self, env)