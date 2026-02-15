"""Goal-reaching termination terms."""

from __future__ import annotations

from typing import TYPE_CHECKING

import torch

from mjlab.sensor import ContactSensor

if TYPE_CHECKING:
  from mjlab.envs import ManagerBasedRlEnv


def illegal_contact(env: ManagerBasedRlEnv, sensor_name: str) -> torch.Tensor:
  """Terminate on non-foot ground contact."""
  sensor: ContactSensor = env.scene[sensor_name]
  assert sensor.data.found is not None
  return torch.any(sensor.data.found, dim=-1)


def goal_reached(
  env: ManagerBasedRlEnv,
  command_name: str,
  distance_threshold: float = 0.3,
  heading_threshold: float = 0.3,
) -> torch.Tensor:
  """Terminate (success) when goal position and heading are reached.

  This is a soft termination — the command term will resample a new goal
  if `resample_on_reach` is enabled. Use this for logging / metrics.
  """
  command = env.command_manager.get_command(command_name)
  assert command is not None
  pos_dist = torch.norm(command[:, :2], dim=1)
  heading_err = torch.abs(command[:, 2])
  return (pos_dist < distance_threshold) & (heading_err < heading_threshold)