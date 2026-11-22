"""Tests for the sensor-based tracking anchor orientation observation."""

from __future__ import annotations

from typing import TYPE_CHECKING, cast
from unittest.mock import Mock

import mujoco
import numpy as np
import pytest
import torch
from conftest import get_test_device

from mjlab.entity import EntityCfg
from mjlab.envs.mdp import dr
from mjlab.managers.observation_manager import ObservationTermCfg
from mjlab.managers.scene_entity_config import SceneEntityCfg
from mjlab.scene import Scene, SceneCfg
from mjlab.sim.sim import Simulation, SimulationCfg
from mjlab.tasks.tracking.mdp import (
  motion_anchor_ori_b,
  motion_anchor_ori_b_from_sensor,
)
from mjlab.utils.lab_api.math import matrix_from_quat, quat_from_euler_xyz

if TYPE_CHECKING:
  from mjlab.envs import ManagerBasedRlEnv

# Half turn about (0, -1, 0, 1)/sqrt(2), the IMU mount that motivated this term.
_HALF_TURN = "0 -1 0 1"


@pytest.fixture(scope="module")
def device():
  return get_test_device()


def _robot_xml(site_quat: str) -> str:
  return f"""
    <mujoco>
      <worldbody>
        <body name="torso" pos="0 0 1">
          <freejoint name="free_joint"/>
          <geom type="box" size="0.2 0.2 0.1" mass="5.0"/>
          <site name="imu" pos="0.05 0 0" quat="{site_quat}"/>
          <body name="arm" pos="0 0.3 0">
            <joint name="shoulder" type="hinge" axis="0 1 0"/>
            <geom type="capsule" size="0.03" fromto="0 0 0 0 0 -0.2" mass="0.5"/>
            <site name="arm_imu"/>
          </body>
        </body>
      </worldbody>
      <sensor>
        <framequat name="imu_quat" objtype="site" objname="imu"/>
        <framequat name="arm_imu_quat" objtype="site" objname="arm_imu"/>
      </sensor>
    </mujoco>
  """


def _make_env(
  device: str,
  site_quat: str,
  robot_quat: torch.Tensor,
  anchor_quat: torch.Tensor,
) -> ManagerBasedRlEnv:
  """Build a scene and an env stub whose motion command points at the torso."""
  num_envs = robot_quat.shape[0]
  xml = _robot_xml(site_quat)
  entity_cfg = EntityCfg(spec_fn=lambda: mujoco.MjSpec.from_string(xml))
  scene = Scene(
    SceneCfg(num_envs=num_envs, env_spacing=3.0, entities={"robot": entity_cfg}),
    device,
  )
  sim = Simulation(
    num_envs=num_envs,
    cfg=SimulationCfg(njmax=20),
    model=scene.compile(),
    device=device,
  )
  scene.initialize(sim.mj_model, sim.model, sim.data)
  sim.expand_model_fields(("site_quat",))

  robot = scene["robot"]
  root_state = robot.data.default_root_state.clone()
  root_state[:, 3:7] = robot_quat.to(device)
  robot.write_root_state_to_sim(root_state)
  sim.forward()

  anchor_index = robot.body_names.index("torso")
  anchor_pos_w = robot.data.body_link_pos_w[:, anchor_index]
  command = Mock(
    robot=robot,
    robot_anchor_body_index=anchor_index,
    robot_anchor_pos_w=anchor_pos_w,
    robot_anchor_quat_w=robot.data.body_link_quat_w[:, anchor_index],
    anchor_pos_w=anchor_pos_w,
    anchor_quat_w=anchor_quat.to(device),
  )
  command.cfg.anchor_body_name = "torso"
  env = Mock(scene=scene, sim=sim, num_envs=num_envs, device=device)
  env.command_manager.get_term.return_value = command
  return cast("ManagerBasedRlEnv", env)


def _sensor_term(
  env: ManagerBasedRlEnv, sensor_name: str = "robot/imu_quat"
) -> torch.Tensor:
  cfg = ObservationTermCfg(
    func=motion_anchor_ori_b_from_sensor,
    params={"command_name": "motion", "sensor_name": sensor_name},
  )
  return motion_anchor_ori_b_from_sensor(cfg, env)(env, **cfg.params)


def _random_quat(n: int) -> torch.Tensor:
  return quat_from_euler_xyz(*torch.rand(3, n).mul(2 * torch.pi).sub(torch.pi))


@pytest.mark.parametrize("site_quat", ["1 0 0 0", _HALF_TURN])
def test_sensor_term_is_the_body_term_in_the_site_frame(device, site_quat):
  """The reference-to-robot rotation, expressed in the IMU site frame."""
  torch.manual_seed(0)
  robot_quat, anchor_quat = _random_quat(4), _random_quat(4)
  env = _make_env(device, site_quat, robot_quat, anchor_quat)

  site_mat = np.zeros(9)
  site_quat_np = np.array(site_quat.split(), dtype=np.float64)
  mujoco.mju_quat2Mat(site_mat, site_quat_np / np.linalg.norm(site_quat_np))
  r_site = torch.tensor(site_mat.reshape(3, 3), dtype=torch.float32, device=device)
  r_body = matrix_from_quat(robot_quat.to(device)).transpose(-1, -2) @ matrix_from_quat(
    anchor_quat.to(device)
  )
  expected = r_site.T @ r_body @ r_site

  obs = _sensor_term(env)
  torch.testing.assert_close(obs, expected[..., :2].reshape(4, -1), atol=1e-5, rtol=0)
  if site_quat == "1 0 0 0":
    torch.testing.assert_close(
      obs, motion_anchor_ori_b(env, "motion"), atol=1e-5, rtol=0
    )


@pytest.mark.filterwarnings(
  "ignore:Use of index_put_ on expanded tensors is deprecated:UserWarning"
)
def test_site_quat_randomization_reaches_the_sensor_term_only(device):
  """IMU mounting DR shows up in the sensor term but not in the body term."""
  quat = _random_quat(4)
  env = _make_env(device, _HALF_TURN, quat, quat)
  identity = torch.tensor([1.0, 0.0, 0.0, 1.0, 0.0, 0.0], device=device).expand(4, -1)
  torch.testing.assert_close(_sensor_term(env), identity, atol=1e-5, rtol=0)

  torch.manual_seed(0)
  dr.site_quat(
    env,
    env_ids=None,
    roll_range=(-0.3, 0.3),
    pitch_range=(-0.3, 0.3),
    yaw_range=(-0.3, 0.3),
    asset_cfg=SceneEntityCfg("robot", site_names=("imu",)),
  )
  env.sim.forward()

  after = _sensor_term(env)
  assert (after - identity).abs().amax(dim=-1).min() > 0.01
  assert torch.unique(after, dim=0).shape[0] == 4
  torch.testing.assert_close(
    motion_anchor_ori_b(env, "motion"), identity, atol=1e-5, rtol=0
  )


def test_sensor_term_rejects_a_site_off_the_anchor_body(device):
  quat = _random_quat(1)
  env = _make_env(device, "1 0 0 0", quat, quat)
  with pytest.raises(ValueError, match="anchor body 'torso'"):
    _sensor_term(env, "robot/arm_imu_quat")
