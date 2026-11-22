from __future__ import annotations

from typing import TYPE_CHECKING, cast

import mujoco
import torch

from mjlab.sensor import BuiltinSensor
from mjlab.utils.lab_api.math import (
  matrix_from_quat,
  quat_inv,
  quat_mul,
  subtract_frame_transforms,
)

from .commands import MotionCommand

if TYPE_CHECKING:
  from mjlab.envs import ManagerBasedRlEnv
  from mjlab.managers.observation_manager import ObservationTermCfg


def motion_anchor_pos_b(env: ManagerBasedRlEnv, command_name: str) -> torch.Tensor:
  command = cast(MotionCommand, env.command_manager.get_term(command_name))

  pos, _ = subtract_frame_transforms(
    command.robot_anchor_pos_w,
    command.robot_anchor_quat_w,
    command.anchor_pos_w,
    command.anchor_quat_w,
  )

  return pos.view(env.num_envs, -1)


def motion_anchor_ori_b(env: ManagerBasedRlEnv, command_name: str) -> torch.Tensor:
  command = cast(MotionCommand, env.command_manager.get_term(command_name))

  _, ori = subtract_frame_transforms(
    command.robot_anchor_pos_w,
    command.robot_anchor_quat_w,
    command.anchor_pos_w,
    command.anchor_quat_w,
  )
  mat = matrix_from_quat(ori)
  return mat[..., :2].reshape(mat.shape[0], -1)


class motion_anchor_ori_b_from_sensor:
  """Reference anchor orientation in the frame of a ``framequat`` IMU sensor.

  :func:`motion_anchor_ori_b` reads the anchor body orientation, so a deployed policy
  must undo the IMU mounting rotation itself, and ``dr.site_quat`` on the IMU site
  never reaches the observation. This term reads the robot orientation from a
  ``framequat`` sensor on a site attached to the anchor body, and moves the reference
  into the same frame with the site's nominal mounting rotation from the model. The
  reference ignores ``dr.site_quat``, as a deployed policy only knows the nominal
  mount. With an unrotated site, it equals :func:`motion_anchor_ori_b`.
  """

  def __init__(self, cfg: ObservationTermCfg, env: ManagerBasedRlEnv):
    command = cast(
      MotionCommand, env.command_manager.get_term(cfg.params["command_name"])
    )
    mj_model = env.sim.mj_model
    sensor = mj_model.sensor(cfg.params["sensor_name"])
    if (
      sensor.type[0] != mujoco.mjtSensor.mjSENS_FRAMEQUAT
      or sensor.objtype[0] != mujoco.mjtObj.mjOBJ_SITE
      or sensor.refid[0] != -1
    ):
      raise ValueError(
        f"Sensor '{sensor.name}' must be a framequat on a site with no reference frame."
      )
    site_id = sensor.objid[0]
    anchor_body_id = command.robot.indexing.body_ids[command.robot_anchor_body_index]
    if mj_model.site_bodyid[site_id] != anchor_body_id:
      raise ValueError(
        f"Sensor '{sensor.name}' must be on a site attached to the anchor body "
        f"'{command.cfg.anchor_body_name}'."
      )
    self.site_quat_b = torch.tensor(
      mj_model.site_quat[site_id], dtype=torch.float32, device=env.device
    )

  def __call__(
    self, env: ManagerBasedRlEnv, command_name: str, sensor_name: str
  ) -> torch.Tensor:
    command = cast(MotionCommand, env.command_manager.get_term(command_name))
    sensor = env.scene[sensor_name]
    assert isinstance(sensor, BuiltinSensor)

    site_quat_b = self.site_quat_b.expand_as(command.anchor_quat_w)
    ref_site_quat_w = quat_mul(command.anchor_quat_w, site_quat_b)
    ori = quat_mul(quat_inv(sensor.data), ref_site_quat_w)
    mat = matrix_from_quat(ori)
    return mat[..., :2].reshape(mat.shape[0], -1)


def robot_body_pos_b(env: ManagerBasedRlEnv, command_name: str) -> torch.Tensor:
  command = cast(MotionCommand, env.command_manager.get_term(command_name))

  num_bodies = len(command.cfg.body_names)
  pos_b, _ = subtract_frame_transforms(
    command.robot_anchor_pos_w[:, None, :].repeat(1, num_bodies, 1),
    command.robot_anchor_quat_w[:, None, :].repeat(1, num_bodies, 1),
    command.robot_body_pos_w,
    command.robot_body_quat_w,
  )

  return pos_b.view(env.num_envs, -1)


def robot_body_ori_b(env: ManagerBasedRlEnv, command_name: str) -> torch.Tensor:
  command = cast(MotionCommand, env.command_manager.get_term(command_name))

  num_bodies = len(command.cfg.body_names)
  _, ori_b = subtract_frame_transforms(
    command.robot_anchor_pos_w[:, None, :].repeat(1, num_bodies, 1),
    command.robot_anchor_quat_w[:, None, :].repeat(1, num_bodies, 1),
    command.robot_body_pos_w,
    command.robot_body_quat_w,
  )
  mat = matrix_from_quat(ori_b)
  return mat[..., :2].reshape(mat.shape[0], -1)
