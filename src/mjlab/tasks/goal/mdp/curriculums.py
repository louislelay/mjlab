"""Goal-reaching curriculum terms.

Provides terrain difficulty progression and goal distance curriculum.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypedDict

import torch

from mjlab.entity import Entity
from mjlab.managers.scene_entity_config import SceneEntityCfg

from .commands import GoalPositionCommandCfg

if TYPE_CHECKING:
  from mjlab.envs import ManagerBasedRlEnv

_DEFAULT_SCENE_CFG = SceneEntityCfg("robot")


def terrain_levels_goal(
  env: ManagerBasedRlEnv,
  env_ids: torch.Tensor,
  command_name: str,
  asset_cfg: SceneEntityCfg = _DEFAULT_SCENE_CFG,
) -> torch.Tensor:
  """Progress terrain difficulty based on goal-reaching success.

  Robots that reach their goal (small final distance) progress to harder
  terrains. Robots that end far from goal regress to easier terrains.
  """
  asset: Entity = env.scene[asset_cfg.name]
  terrain = env.scene.terrain
  assert terrain is not None
  terrain_generator = terrain.cfg.terrain_generator
  assert terrain_generator is not None

  # Use the goal command term to get current distance.
  command = env.command_manager.get_command(command_name)
  assert command is not None
  goal_dist = torch.norm(command[env_ids, :2], dim=1)

  # Progress if close to goal, regress if far.
  move_up = goal_dist < 0.5
  move_down = goal_dist > 3.0
  move_down = move_down & ~move_up

  terrain.update_env_origins(env_ids, move_up, move_down)
  return torch.mean(terrain.terrain_levels.float())


class GoalDistStage(TypedDict):
  step: int
  goal_dist: tuple[float, float]


def goal_distance_curriculum(
  env: ManagerBasedRlEnv,
  env_ids: torch.Tensor,
  command_name: str,
  stages: list[GoalDistStage],
) -> dict[str, torch.Tensor]:
  """Progressively increase goal sampling distance over training."""
  del env_ids
  from typing import cast

  command_term = env.command_manager.get_term(command_name)
  assert command_term is not None
  cfg = cast(GoalPositionCommandCfg, command_term.cfg)
  for stage in stages:
    if env.common_step_counter > stage["step"]:
      cfg.ranges.goal_dist = stage["goal_dist"]
  return {
    "goal_dist_min": torch.tensor(cfg.ranges.goal_dist[0]),
    "goal_dist_max": torch.tensor(cfg.ranges.goal_dist[1]),
  }