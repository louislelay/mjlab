"""Tests for the offscreen renderer."""

import mujoco
import numpy as np
import pytest

from mjlab.viewer.offscreen_renderer import OffscreenRenderer, _FilamentScene
from mjlab.viewer.viewer_config import ViewerConfig

_XML = """
<mujoco>
  <worldbody>
    <light pos="0 0 3" dir="0 0 -1"/>
    <geom type="plane" size="2 2 0.1" rgba="0.5 0.5 0.5 1"/>
    <body pos="0 0 0.2">
      <freejoint/>
      <geom type="box" size="0.1 0.1 0.1" rgba="1 0 0 1"/>
    </body>
  </worldbody>
</mujoco>
"""


def _render_frames(frames: list[list[mujoco.MjvGeom]]) -> list[np.ndarray]:
  """Render one image per overlay list, reusing a single Filament scene."""
  model = mujoco.MjModel.from_xml_string(_XML)
  data = mujoco.MjData(model)
  mujoco.mj_forward(model, data)
  camera = mujoco.MjvCamera()
  mujoco.mjv_defaultFreeCamera(model, camera)
  camera.distance, camera.elevation = 2.0, -30.0
  overlay = mujoco.MjvScene(model, maxgeom=10)
  pixels = np.zeros((96, 128, 3), dtype=np.uint8)
  scene = _FilamentScene(model, mujoco.MjvOption(), pixels)
  mujoco.mjv_updateCamera(model, data, camera, overlay)
  scene.update_world(data)
  images = []
  for geoms in frames:
    scene.draw_overlays(geoms)
    scene.render(overlay.camera[0], shadows=True, reflections=True)
    images.append(pixels.copy())
  return images


def _green_sphere() -> mujoco.MjvGeom:
  geom = mujoco.MjvGeom()
  mujoco.mjv_initGeom(
    geom,
    mujoco.mjtGeom.mjGEOM_SPHERE,
    np.full(3, 0.15),
    np.array([0.4, 0.0, 0.3]),
    np.eye(3).ravel(),
    np.array([0.0, 1.0, 0.0, 1.0], dtype=np.float32),
  )
  return geom


def _count_green(pixels: np.ndarray) -> int:
  rgb = pixels.astype(int)
  return int(np.sum((rgb[..., 1] > 120) & (rgb[..., 0] < 80) & (rgb[..., 2] < 80)))


def test_filament_overlays_show_then_hide():
  plain, with_sphere, cleared = _render_frames([[], [_green_sphere()], []])
  assert plain.mean() > 0
  assert _count_green(plain) == 0
  assert _count_green(with_sphere) > 50
  assert _count_green(cleared) == 0


def test_env_ids_clamps_when_fewer_envs_than_requested():
  # Default max_extra_envs=2 with a single env must not raise (csv_to_npz and
  # single-env video recording rely on this).
  cfg = ViewerConfig(max_extra_envs=2)
  ids = OffscreenRenderer._get_env_ids(cfg, np.zeros((1, 3)))
  assert ids == (0,)


def test_env_ids_primary_is_env_idx_despite_identical_origins():
  # With identical origins, distance ties must not evict env_idx from the set.
  cfg = ViewerConfig(env_idx=3, max_extra_envs=2)
  ids = OffscreenRenderer._get_env_ids(cfg, np.zeros((8, 3)))
  assert ids[0] == 3
  assert len(ids) == 3
  assert len(set(ids)) == 3


def test_env_ids_selects_nearest_neighbors():
  cfg = ViewerConfig(env_idx=0, max_extra_envs=2)
  origins = np.array(
    [[0.0, 0.0, 0.0], [10.0, 0.0, 0.0], [1.0, 0.0, 0.0], [2.0, 0.0, 0.0]]
  )
  ids = OffscreenRenderer._get_env_ids(cfg, origins)
  assert ids == (0, 2, 3)


def test_env_ids_out_of_range_env_idx_is_clamped():
  cfg = ViewerConfig(env_idx=99, max_extra_envs=0)
  ids = OffscreenRenderer._get_env_ids(cfg, np.zeros((4, 3)))
  assert ids == (3,)


def test_env_ids_negative_max_extra_envs_raises():
  cfg = ViewerConfig(max_extra_envs=-1)
  with pytest.raises(ValueError, match="max_extra_envs"):
    OffscreenRenderer._get_env_ids(cfg, np.zeros((4, 3)))
