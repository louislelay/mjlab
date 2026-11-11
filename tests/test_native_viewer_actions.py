"""Tests for native viewer custom action dispatch."""

from __future__ import annotations

from unittest.mock import MagicMock

import mujoco
import numpy as np
from mujoco.studio.dear_imgui import dear_imgui as imgui

from mjlab.viewer.base import ViewerAction
from mjlab.viewer.native import keys
from mjlab.viewer.native.studio import (
  KEY_CODES,
  KeyEvent,
  MjlabSimPlugin,
  drawable_overlays,
)
from mjlab.viewer.native.viewer import NativeMujocoViewer


def _make_viewer(num_envs: int = 3) -> NativeMujocoViewer:
  env = MagicMock()
  env.cfg.viewer.env_idx = 0
  env.unwrapped.num_envs = num_envs
  return NativeMujocoViewer(env, MagicMock())


def test_toggle_actions_dispatch_by_action_enum():
  v = _make_viewer()

  assert not v._show_plots
  assert v._handle_custom_action(ViewerAction.TOGGLE_PLOTS, None)
  assert v._show_plots

  assert v._show_debug_vis
  assert v._handle_custom_action(ViewerAction.TOGGLE_DEBUG_VIS, None)
  assert not v._show_debug_vis

  assert not v._show_all_envs
  assert v._handle_custom_action(ViewerAction.TOGGLE_SHOW_ALL_ENVS, None)
  assert v._show_all_envs


def test_prev_next_env_actions_wrap_and_succeed():
  v = _make_viewer(num_envs=3)
  v.env_idx = 0
  assert v._handle_custom_action(ViewerAction.PREV_ENV, None)
  assert v.env_idx == 2
  assert v._handle_custom_action(ViewerAction.NEXT_ENV, None)
  assert v.env_idx == 0


def test_imgui_keys_map_to_glfw_codes():
  assert KEY_CODES[imgui.Key.Space] == keys.KEY_SPACE
  assert KEY_CODES[imgui.Key.Enter] == keys.KEY_ENTER
  assert KEY_CODES[imgui.Key.RightArrow] == keys.KEY_RIGHT
  assert KEY_CODES[imgui.Key.Period] == keys.KEY_PERIOD
  assert KEY_CODES[imgui.Key.P] == keys.KEY_P


def test_key_codes_dispatch_viewer_requests():
  v = _make_viewer()
  user_keys: list[int] = []
  v.user_key_callback = user_keys.append

  v._safe_key_callback(keys.KEY_P)
  v._safe_key_callback(keys.KEY_SPACE)

  actions = [a for a, _ in v._actions]
  assert actions == [ViewerAction.TOGGLE_PLOTS, ViewerAction.TOGGLE_PAUSE]
  assert user_keys == [keys.KEY_P, keys.KEY_SPACE]


def test_drawable_overlays_drops_asset_geoms():
  scn = mujoco.MjvScene(mujoco.MjModel.from_xml_string("<mujoco/>"), maxgeom=3)
  for geom, geom_type in zip(
    scn.geoms,
    (
      mujoco.mjtGeom.mjGEOM_SPHERE,
      mujoco.mjtGeom.mjGEOM_MESH,
      mujoco.mjtGeom.mjGEOM_ARROW,
    ),
    strict=True,
  ):
    geom.type = geom_type
  scn.ngeom = 3

  kept = drawable_overlays(scn.geoms[: scn.ngeom])

  assert [g.type for g in kept] == [
    mujoco.mjtGeom.mjGEOM_SPHERE,
    mujoco.mjtGeom.mjGEOM_ARROW,
  ]
  kept[0].rgba[:] = 0.5
  assert not np.allclose(scn.geoms[0].rgba, 0.5)


def test_sim_plugin_queues_keys_until_popped():
  sim = MjlabSimPlugin()
  sim.on_key(KeyEvent(key=keys.KEY_R))
  sim.on_key(KeyEvent(key=keys.KEY_A))
  assert sim.pop_keys() == [keys.KEY_R, keys.KEY_A]
  assert sim.pop_keys() == []
