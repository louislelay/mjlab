"""Goal-reaching reward terms.

Implements the AME-2 reward structure for goal-reaching locomotion:
  - Goal position tracking (exponential)
  - Goal heading tracking (exponential)
  - Moving-to-goal (velocity projection)
  - Standing-at-goal (penalize velocity near goal)

Plus regularization terms reused from velocity task.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

import torch

from mjlab.entity import Entity
from mjlab.managers.scene_entity_config import SceneEntityCfg
from mjlab.sensor import ContactSensor
from mjlab.utils.lab_api.math import quat_apply_inverse, wrap_to_pi

if TYPE_CHECKING:
  from mjlab.envs import ManagerBasedRlEnv

_DEFAULT_ASSET_CFG = SceneEntityCfg("robot")


# ---------------------------------------------------------------------------
# Goal-reaching rewards
# ---------------------------------------------------------------------------


def goal_position_tracking(
  env: ManagerBasedRlEnv,
  command_name: str,
  std: float,
  asset_cfg: SceneEntityCfg = _DEFAULT_ASSET_CFG,
) -> torch.Tensor:
  """Exponential reward for proximity to goal position.

  r = exp(-||goal_xy_b||² / σ²)

  Uses the body-frame goal displacement from the command term (first 2 dims).
  """
  command = env.command_manager.get_command(command_name)
  assert command is not None
  goal_xy_b = command[:, :2]  # [dx_b, dy_b]
  dist_sq = torch.sum(torch.square(goal_xy_b), dim=1)
  return torch.exp(-dist_sq / std**2)


def goal_heading_tracking(
  env: ManagerBasedRlEnv,
  command_name: str,
  std: float,
) -> torch.Tensor:
  """Exponential reward for matching target heading.

  r = exp(-dθ² / σ²)

  Uses the heading error from the command term (3rd dim).
  """
  command = env.command_manager.get_command(command_name)
  assert command is not None
  heading_error = command[:, 2]  # dθ
  return torch.exp(-torch.square(heading_error) / std**2)


def moving_to_goal(
  env: ManagerBasedRlEnv,
  command_name: str,
  asset_cfg: SceneEntityCfg = _DEFAULT_ASSET_CFG,
) -> torch.Tensor:
  """Reward for velocity projected towards the goal.

  r = clamp(v_b · normalize(goal_xy_b), min=0)

  Encourages the robot to move towards the goal. Only positive projection
  is rewarded (no penalty for moving away — that's handled by other terms).
  """
  asset: Entity = env.scene[asset_cfg.name]
  command = env.command_manager.get_command(command_name)
  assert command is not None

  goal_xy_b = command[:, :2]  # [B, 2]
  goal_dist = torch.norm(goal_xy_b, dim=1, keepdim=True).clamp(min=1e-3)
  goal_dir_b = goal_xy_b / goal_dist  # [B, 2] normalized direction

  vel_xy_b = asset.data.root_link_lin_vel_b[:, :2]  # [B, 2]
  projection = torch.sum(vel_xy_b * goal_dir_b, dim=1)  # [B]

  return torch.clamp(projection, min=0.0)


def standing_at_goal(
  env: ManagerBasedRlEnv,
  command_name: str,
  distance_threshold: float = 0.5,
  asset_cfg: SceneEntityCfg = _DEFAULT_ASSET_CFG,
) -> torch.Tensor:
  """Penalize velocity when close to the goal.

  When ||goal_xy_b|| < threshold, penalize ||v_b_xy||².
  Encourages the robot to stop once it reaches the goal.
  """
  asset: Entity = env.scene[asset_cfg.name]
  command = env.command_manager.get_command(command_name)
  assert command is not None

  goal_xy_b = command[:, :2]
  goal_dist = torch.norm(goal_xy_b, dim=1)
  near_goal = (goal_dist < distance_threshold).float()

  vel_xy_b = asset.data.root_link_lin_vel_b[:, :2]
  vel_sq = torch.sum(torch.square(vel_xy_b), dim=1)

  return vel_sq * near_goal


# ---------------------------------------------------------------------------
# Regularization rewards (adapted from velocity task)
# ---------------------------------------------------------------------------


def flat_orientation(
  env: ManagerBasedRlEnv,
  std: float,
  asset_cfg: SceneEntityCfg = _DEFAULT_ASSET_CFG,
) -> torch.Tensor:
  """Reward flat base orientation."""
  asset: Entity = env.scene[asset_cfg.name]
  if asset_cfg.body_ids:
    body_quat_w = asset.data.body_link_quat_w[:, asset_cfg.body_ids, :].squeeze(1)
    gravity_w = asset.data.gravity_vec_w
    projected_gravity_b = quat_apply_inverse(body_quat_w, gravity_w)
    xy_squared = torch.sum(torch.square(projected_gravity_b[:, :2]), dim=1)
  else:
    xy_squared = torch.sum(torch.square(asset.data.projected_gravity_b[:, :2]), dim=1)
  return torch.exp(-xy_squared / std**2)


def feet_clearance(
  env: ManagerBasedRlEnv,
  target_height: float,
  command_name: str,
  command_threshold: float = 0.01,
  asset_cfg: SceneEntityCfg = _DEFAULT_ASSET_CFG,
) -> torch.Tensor:
  """Penalize deviation from target clearance height, weighted by foot velocity.

  Active only when moving (goal distance > threshold).
  """
  asset: Entity = env.scene[asset_cfg.name]
  command = env.command_manager.get_command(command_name)
  assert command is not None

  foot_z = asset.data.site_pos_w[:, asset_cfg.site_ids, 2]
  foot_vel_xy = asset.data.site_lin_vel_w[:, asset_cfg.site_ids, :2]
  vel_norm = torch.norm(foot_vel_xy, dim=-1)
  delta = torch.abs(foot_z - target_height)
  cost = torch.sum(delta * vel_norm, dim=1)

  # Gate on whether robot should be moving (far enough from goal).
  goal_dist = torch.norm(command[:, :2], dim=1)
  active = (goal_dist > command_threshold).float()
  return cost * active


def feet_slip(
  env: ManagerBasedRlEnv,
  sensor_name: str,
  command_name: str,
  command_threshold: float = 0.01,
  asset_cfg: SceneEntityCfg = _DEFAULT_ASSET_CFG,
) -> torch.Tensor:
  """Penalize foot sliding (xy velocity while in contact)."""
  asset: Entity = env.scene[asset_cfg.name]
  contact_sensor: ContactSensor = env.scene[sensor_name]
  command = env.command_manager.get_command(command_name)
  assert command is not None

  goal_dist = torch.norm(command[:, :2], dim=1)
  active = (goal_dist > command_threshold).float()

  assert contact_sensor.data.found is not None
  in_contact = (contact_sensor.data.found > 0).float()
  foot_vel_xy = asset.data.site_lin_vel_w[:, asset_cfg.site_ids, :2]
  vel_xy_norm_sq = torch.sum(torch.square(foot_vel_xy), dim=-1)
  cost = torch.sum(vel_xy_norm_sq * in_contact, dim=1) * active
  return cost


def self_collision_cost(env: ManagerBasedRlEnv, sensor_name: str) -> torch.Tensor:
  """Penalize self-collisions."""
  sensor: ContactSensor = env.scene[sensor_name]
  assert sensor.data.found is not None
  return sensor.data.found.squeeze(-1)