"""Environment viewer built on MuJoCo Studio.

Overview
--------
The simulation runs on the GPU via mujoco_warp, but MuJoCo Studio displays CPU
``MjModel`` and ``MjData`` structures. Each frame, this module copies the GPU
state for one environment into CPU buffers, calls ``mj_forward`` to recompute
kinematics and contacts, and hands the result to Studio's viewer thread via
``ViewerHandle.sync``. Contacts visible in the viewer are computed by C MuJoCo
on the CPU, not by mujoco_warp on the GPU.

The per frame sync has four steps:

1. ``_sync_env_state_to_mjdata``: copy ``qpos``, ``qvel``, ``mocap``, and
   ``xfrc_applied`` from GPU tensors into CPU ``MjData``.
2. ``mj_forward``: recompute kinematics, collisions, and derived quantities.
3. ``_sync_model_fields``: if domain randomization expanded visual fields
   (geom colors, body poses, camera parameters, etc.), copy the per world
   values from GPU ``sim.model`` into CPU ``MjModel``.
4. ``handle.sync()``: send the integration state to the viewer thread, along
   with a :class:`~mjlab.viewer.native.studio.FrameSnapshot` carrying overlay
   geoms, randomized model fields, the status text and reward plots.

For multi environment scenes, steps 1 and 2 are repeated for neighboring
environments into a secondary ``MjData`` (``self.vd``), and their geoms are
added to the snapshot with ``mjv_addGeoms``.

External force channels
-----------------------
MuJoCo sums two external force inputs during forward dynamics:

* ``xfrc_applied``: Cartesian forces per body (GPU to CPU, for rendering).
* ``qfrc_applied``: generalized forces per DoF (CPU to GPU, for mouse input).

Programmatic forces (e.g. ``apply_body_impulse``) write to ``xfrc_applied``
on the GPU and flow one way to the CPU ``MjData`` for visualization. Mouse
perturbation forces flow the opposite direction: the viewer thread sends its
``MjvPerturb``, this module computes the force on the CPU via
``mjv_applyPerturbForce``, converts it to joint space with ``mj_applyFT``, and
writes it to ``qfrc_applied`` on the GPU. Each field flows in one direction
only, so the two sources never overwrite each other.

On macOS, MuJoCo Studio cannot open a desktop window from Python (AppKit
requires windows on the main thread, while Studio runs its viewer on a
background thread), so the viewer defaults to Studio's web viewer there and
opens it in a browser tab.
"""

from __future__ import annotations

import copy
from collections import deque
from dataclasses import dataclass
from typing import TYPE_CHECKING, Callable, Optional, Protocol

import mujoco
import numpy as np
import torch
from mujoco.studio import launch_passive, viewer_handle, viewer_protocol

from mjlab.viewer.base import (
  BaseViewer,
  EnvProtocol,
  PolicyProtocol,
  VerbosityLevel,
  ViewerAction,
)
from mjlab.viewer.model_sync import (
  VIEWER_INERTIAL_FIELDS,
  VIEWER_MODEL_FIELDS,
  disable_model_sameframe_shortcuts,
  sync_model_fields,
)
from mjlab.viewer.native.keys import (
  KEY_A,
  KEY_COMMA,
  KEY_ENTER,
  KEY_EQUAL,
  KEY_MINUS,
  KEY_P,
  KEY_PERIOD,
  KEY_R,
  KEY_RIGHT,
  KEY_SPACE,
)
from mjlab.viewer.native.studio import (
  FrameSnapshot,
  MjlabSimPlugin,
  MjlabViewerPlugin,
  RewardPlot,
  ViewerSettings,
  default_gfx,
)
from mjlab.viewer.native.visualizer import MujocoNativeDebugVisualizer

if TYPE_CHECKING:
  from mjlab.entity import Entity

_MAX_OVERLAY_GEOMS = 10_000

_KEY_ACTIONS: dict[int, str] = {
  KEY_COMMA: "PREV_ENV",
  KEY_PERIOD: "NEXT_ENV",
  KEY_P: "TOGGLE_PLOTS",
  KEY_R: "TOGGLE_DEBUG_VIS",
  KEY_A: "TOGGLE_SHOW_ALL_ENVS",
}


@dataclass(frozen=True)
class PlotCfg:
  """Reward plot configuration."""

  history: int = 300
  """Points kept per reward term."""
  max_plots: int = 12
  """Maximum number of reward terms plotted."""


class _SimDataProtocol(Protocol):
  qpos: "_TensorArrayProtocol"
  qvel: "_TensorArrayProtocol"
  mocap_pos: "_TensorArrayProtocol"
  mocap_quat: "_TensorArrayProtocol"
  ctrl: "_TensorArrayProtocol"
  xfrc_applied: "_TensorArrayProtocol"
  qfrc_applied: "_TensorArrayProtocol"


class _CpuArrayProtocol(Protocol):
  def cpu(self) -> "_CpuArrayProtocol": ...
  def numpy(self) -> np.ndarray: ...


class _TensorArrayProtocol(Protocol):
  def __getitem__(self, idx: int) -> _CpuArrayProtocol: ...


class _SimModelProtocol(Protocol):
  def __getattr__(self, name: str) -> object: ...


class _SimProtocol(Protocol):
  data: _SimDataProtocol
  model: _SimModelProtocol
  expanded_fields: set[str]


class NativeMujocoViewer(BaseViewer):
  """Desktop viewer that displays one environment in a MuJoCo Studio window."""

  def __init__(
    self,
    env: EnvProtocol,
    policy: PolicyProtocol,
    frame_rate: float = 60.0,
    key_callback: Optional[Callable[[int], None]] = None,
    plot_cfg: PlotCfg | None = None,
    enable_perturbations: bool = True,
    verbosity: VerbosityLevel = VerbosityLevel.SILENT,
    gfx: str | None = None,
  ):
    """Create the viewer.

    Args:
      env: Environment to display.
      policy: Policy that produces actions from observations.
      frame_rate: Display refresh rate in Hz.
      key_callback: Called with the GLFW key code of every key press.
      plot_cfg: Reward plot configuration.
      enable_perturbations: Whether mouse dragging applies forces to bodies.
      verbosity: Logging verbosity.
      gfx: MuJoCo Studio graphics mode, e.g. ``"opengl"``, ``"vulkan"`` or
        ``"web"``. Defaults to
        :func:`~mjlab.viewer.native.studio.default_gfx`.
    """
    super().__init__(env, policy, frame_rate, verbosity)
    self.user_key_callback = key_callback
    self.enable_perturbations = enable_perturbations
    self.gfx = default_gfx() if gfx is None else gfx

    self.mjm: Optional[mujoco.MjModel] = None
    self.mjd: Optional[mujoco.MjData] = None
    self.handle: Optional[viewer_handle.ViewerHandle] = None
    self.vd: Optional[mujoco.MjData] = None
    self.vopt: Optional[mujoco.MjvOption] = None
    self.scn: Optional[mujoco.MjvScene] = None
    self.catmask: int = mujoco.mjtCatBit.mjCAT_DYNAMIC.value
    self._sim_plugin = MjlabSimPlugin()
    self._camera = mujoco.MjvCamera()

    self._term_names: list[str] = []
    self._histories: dict[str, deque[float]] = {}
    self._show_plots: bool = False
    self._show_debug_vis: bool = True
    self._show_all_envs: bool = False
    self._plot_cfg = plot_cfg or PlotCfg()

    self.env_idx = self.cfg.env_idx

  def setup(self) -> None:
    """Launch the MuJoCo Studio window."""
    sim = self.env.unwrapped.sim
    self.mjm = sim.mj_model
    self.mjd = sim.mj_data
    assert self.mjm is not None and self.mjd is not None
    disable_model_sameframe_shortcuts(self.mjm)
    if self.cfg.fovy is not None:
      self.mjm.vis.global_.fovy = self.cfg.fovy

    if self.env.unwrapped.num_envs > 1:
      self.vd = mujoco.MjData(self.mjm)
    self.vopt = mujoco.MjvOption()
    self.scn = mujoco.MjvScene(self.mjm, maxgeom=_MAX_OVERLAY_GEOMS)

    self._term_names = [
      name
      for name, _ in self.env.unwrapped.reward_manager.get_active_iterable_terms(
        self.env_idx
      )
    ]
    self._init_reward_plots(self._term_names)

    mujoco.mjv_defaultFreeCamera(self.mjm, self._camera)
    self._setup_camera()
    settings = ViewerSettings(
      camera=copy.deepcopy(self._camera),
      shadows=self.cfg.enable_shadows,
      enable_perturbations=self.enable_perturbations,
    )
    config = viewer_protocol.ViewerConfig(
      title="mjlab", gfx=self.gfx, open_browser=self.gfx == "web"
    )
    self.handle = launch_passive.launch(
      config, plugins=[MjlabViewerPlugin(settings), self._sim_plugin]
    )
    self.handle.set_model(self.mjm, data=self.mjd)

    if self.enable_perturbations:
      self.log("[INFO] Interactive perturbations enabled", VerbosityLevel.INFO)

  def is_running(self) -> bool:
    return bool(self.handle and self.handle.is_running())

  def sync_env_to_viewer(self) -> None:
    """Copy env state to the viewer, with overlays and the other envs."""
    handle = self.handle
    assert handle is not None
    assert self.mjm is not None and self.mjd is not None

    if not handle.is_running():
      return

    sim = self.env.unwrapped.sim
    sim_data = sim.data
    self._sync_env_state_to_mjdata(self.mjd, sim_data, self.env_idx)
    self._sync_model_fields(sim, self.env_idx)
    mujoco.mj_forward(self.mjm, self.mjd)

    geoms = self._collect_overlay_geoms(sim, sim_data)
    visual_fields = sim.expanded_fields & VIEWER_MODEL_FIELDS
    model_fields = {
      name: getattr(self.mjm, name).copy() for name in sorted(visual_fields)
    }
    handle.send_to_viewer(
      FrameSnapshot(
        geoms=geoms,
        model_fields=model_fields,
        tracked_body=self._tracked_body(sim),
        status=self._status_text(),
        plots=self._reward_plots(),
      )
    )
    handle.sync(self.mjm, self.mjd)
    for key in self._sim_plugin.pop_keys():
      self._safe_key_callback(key)

  def _status_text(self) -> tuple[str, str]:
    status = self.get_status()
    capped = " [CAPPED]" if status.capped else ""
    labels = "Env\nStep\nStatus\nSpeed\nTarget RT\nActual RT"
    values = (
      f"{self.env_idx + 1}/{self.env.num_envs}\n"
      f"{status.step_count}\n"
      f"{'PAUSED' if status.paused else 'RUNNING'}{capped}\n"
      f"{status.speed_label}\n"
      f"{status.target_realtime:.2f}x\n"
      f"{status.actual_realtime:.2f}x ({status.smoothed_fps:.0f} FPS)"
    )
    return labels, values

  def _reward_plots(self) -> tuple[RewardPlot, ...]:
    if not self._show_plots or not self._term_names:
      return ()
    if not self._is_paused:
      terms = self.env.unwrapped.reward_manager.get_active_iterable_terms(self.env_idx)
      for name, arr in terms:
        value = float(arr[0])
        if name in self._histories and np.isfinite(value):
          self._histories[name].append(value)
    names = self._term_names[: self._plot_cfg.max_plots]
    return tuple(
      RewardPlot(name=name, values=np.fromiter(self._histories[name], dtype=float))
      for name in names
    )

  def _collect_overlay_geoms(
    self, sim: _SimProtocol, sim_data: _SimDataProtocol
  ) -> tuple[mujoco.MjvGeom, ...]:
    """Build debug, env marker and neighbouring env geoms for this frame."""
    scn = self.scn
    assert scn is not None and self.mjm is not None
    scn.ngeom = 0
    if self._show_debug_vis and hasattr(self.env.unwrapped, "update_visualizers"):
      visualizer = MujocoNativeDebugVisualizer(
        scn, self.mjm, self.env_idx, self._show_all_envs
      )
      self.env.unwrapped.update_visualizers(visualizer)
    self._add_env_selection_marker(scn)
    self._add_other_env_geoms(scn, sim, sim_data)
    return tuple(copy.copy(scn.geoms[i]) for i in range(scn.ngeom))

  def _add_env_selection_marker(self, scn: mujoco.MjvScene) -> None:
    """Draw a downward arrow above the selected environment."""
    if self.env.unwrapped.num_envs <= 1 or scn.ngeom >= scn.maxgeom:
      return
    assert self.mjd is not None and self.mjm is not None
    last = self.mjm.nbody - 1
    center = self.mjd.xpos[max(last, 1)].copy()
    arrow_top = center + np.array([0.0, 0.0, 0.4])
    arrow_bottom = center + np.array([0.0, 0.0, 0.15])
    scn.ngeom += 1
    geom = scn.geoms[scn.ngeom - 1]
    geom.category = mujoco.mjtCatBit.mjCAT_DECOR
    mujoco.mjv_initGeom(
      geom=geom,
      type=mujoco.mjtGeom.mjGEOM_ARROW.value,
      size=np.zeros(3),
      pos=np.zeros(3),
      mat=np.zeros(9),
      rgba=np.array([1.0, 0.2, 0.2, 0.8], dtype=np.float32),
    )
    mujoco.mjv_connector(
      geom=geom,
      type=mujoco.mjtGeom.mjGEOM_ARROW.value,
      width=0.02,
      from_=arrow_top,
      to=arrow_bottom,
    )

  def _sync_env_state_to_mjdata(
    self, target_data: mujoco.MjData, sim_data: _SimDataProtocol, env_idx: int
  ) -> None:
    """Copy one environment state from batched sim data into a MjData buffer."""
    assert self.mjm is not None
    if self.mjm.nq > 0:
      target_data.qpos[:] = sim_data.qpos[env_idx].cpu().numpy()
      target_data.qvel[:] = sim_data.qvel[env_idx].cpu().numpy()
    if self.mjm.nu > 0:
      target_data.ctrl[:] = sim_data.ctrl[env_idx].cpu().numpy()
    if self.mjm.nmocap > 0:
      target_data.mocap_pos[:] = sim_data.mocap_pos[env_idx].cpu().numpy()
      target_data.mocap_quat[:] = sim_data.mocap_quat[env_idx].cpu().numpy()
    target_data.xfrc_applied[:] = sim_data.xfrc_applied[env_idx].cpu().numpy()

  def _add_other_env_geoms(
    self,
    scn: mujoco.MjvScene,
    sim: _SimProtocol,
    sim_data: _SimDataProtocol,
  ) -> None:
    """Add the geoms of non-selected environments to the overlay scene."""
    if self.vd is None:
      return
    assert self.mjm is not None and self.vopt is not None

    pert = mujoco.MjvPerturb()
    for i in range(self.env.unwrapped.num_envs):
      if i == self.env_idx:
        continue
      self._sync_env_state_to_mjdata(self.vd, sim_data, i)
      self._sync_model_fields(sim, i)
      mujoco.mj_forward(self.mjm, self.vd)
      mujoco.mjv_addGeoms(self.mjm, self.vd, self.vopt, pert, self.catmask, scn)

    # Restore main env's model fields.
    self._sync_model_fields(sim, self.env_idx)

  def _sync_model_fields(self, sim: _SimProtocol, env_idx: int) -> None:
    """Sync visually-relevant DR'd model fields from GPU to MjModel."""
    assert self.mjm is not None
    fields = sim.expanded_fields & VIEWER_MODEL_FIELDS
    sync_model_fields(self.mjm, sim.model, fields, env_idx)

  def _tracked_body(self, sim: _SimProtocol) -> int:
    """Body whose subtree_com the viewer pins to its frame origin, or -1.

    MuJoCo's tracking camera centers on ``subtree_com[trackbodyid]``, which
    shifts when inertial fields (body_ipos, body_mass) are domain randomized.
    Pinning that entry to ``xpos`` (the body frame origin, unaffected by
    body_ipos) keeps the camera stable.
    """
    if not sim.expanded_fields & VIEWER_INERTIAL_FIELDS:
      return -1
    if self._camera.type != mujoco.mjtCamera.mjCAMERA_TRACKING.value:
      return -1
    return self._camera.trackbodyid

  def sync_viewer_to_env(self) -> None:
    """Sync mouse perturbation to sim via ``qfrc_applied``.

    Mouse perturbation forces are converted from Cartesian body space
    (``xfrc_applied``) to generalized joint space (``qfrc_applied``)
    so that they coexist with programmatic forces on ``xfrc_applied``.
    See the module docstring for details on the channel separation.
    """
    if self.handle is None or self.mjm is None or self.mjd is None:
      return

    sim_data = self.env.unwrapped.sim.data
    pert = self._sim_plugin.perturb

    if not (pert.active != 0 and 0 < pert.select < self.mjm.nbody):
      sim_data.qfrc_applied[self.env_idx] = 0.0
      return

    # Compute mouse perturbation force in Cartesian space.
    mujoco.mjv_applyPerturbForce(self.mjm, self.mjd, pert)

    body_id = pert.select
    force = self.mjd.xfrc_applied[body_id, :3].copy()
    torque = self.mjd.xfrc_applied[body_id, 3:].copy()
    point = self.mjd.xipos[body_id].copy()

    # Convert to generalized forces.
    qfrc = np.zeros(self.mjm.nv)
    mujoco.mj_applyFT(self.mjm, self.mjd, force, torque, point, body_id, qfrc)

    sim_data.qfrc_applied[self.env_idx] = torch.from_numpy(qfrc).to(
      device=sim_data.qfrc_applied.device
    )

    # Clear so _sync_env_state_to_mjdata writes clean programmatic
    # forces next frame.
    self.mjd.xfrc_applied[body_id] = 0.0

  def close(self) -> None:
    """Close viewer and cleanup."""
    handle = self.handle
    self.handle = None
    if handle:
      handle.close()
    self.log("[INFO] MuJoCo viewer closed", VerbosityLevel.INFO)

  def reset_environment(self) -> None:
    """Extend BaseViewer.reset_environment to clear reward histories."""
    super().reset_environment()
    self._clear_histories()

  def _safe_key_callback(self, key: int) -> None:
    """Map a GLFW key code to a viewer action, then call the user callback."""
    if key == KEY_ENTER:
      self.request_reset()
    elif key == KEY_SPACE:
      self.request_toggle_pause()
    elif key == KEY_MINUS:
      self.request_speed_down()
    elif key == KEY_EQUAL:
      self.request_speed_up()
    elif key == KEY_RIGHT:
      self.request_single_step()
    elif key in _KEY_ACTIONS:
      self.request_action(_KEY_ACTIONS[key])

    if self.user_key_callback:
      try:
        self.user_key_callback(key)
      except Exception as e:
        self.log(f"[WARN] user key_callback raised: {e}", VerbosityLevel.INFO)

  def _forward_paused(self) -> None:
    """Run forward kinematics while paused to keep perturbation visuals accurate."""
    if self.mjm is not None and self.mjd is not None:
      mujoco.mj_forward(self.mjm, self.mjd)

  def _handle_custom_action(self, action: ViewerAction, payload: object | None) -> bool:
    del payload
    if action == ViewerAction.PREV_ENV and self.env.unwrapped.num_envs > 1:
      self.env_idx = (self.env_idx - 1) % self.env.unwrapped.num_envs
      self._clear_histories()
      self.log(f"[INFO] Switched to environment {self.env_idx}", VerbosityLevel.INFO)
      return True
    if action == ViewerAction.NEXT_ENV and self.env.unwrapped.num_envs > 1:
      self.env_idx = (self.env_idx + 1) % self.env.unwrapped.num_envs
      self._clear_histories()
      self.log(f"[INFO] Switched to environment {self.env_idx}", VerbosityLevel.INFO)
      return True
    if action == ViewerAction.TOGGLE_PLOTS:
      self._show_plots = not self._show_plots
      self.log(
        f"[INFO] Reward plots {'shown' if self._show_plots else 'hidden'}",
        VerbosityLevel.INFO,
      )
      return True
    if action == ViewerAction.TOGGLE_DEBUG_VIS:
      self._show_debug_vis = not self._show_debug_vis
      self.log(
        f"[INFO] Debug visualization {'shown' if self._show_debug_vis else 'hidden'}",
        VerbosityLevel.INFO,
      )
      return True
    if action == ViewerAction.TOGGLE_SHOW_ALL_ENVS:
      self._show_all_envs = not self._show_all_envs
      self.log(
        f"[INFO] Show all envs {'enabled' if self._show_all_envs else 'disabled'}",
        VerbosityLevel.INFO,
      )
      return True
    return False

  def _setup_camera(self) -> None:
    """Configure the initial camera from the viewer config."""
    if not self.cfg or not hasattr(self.cfg, "origin_type"):
      self._set_camera_auto_track()
      return

    if self.cfg.origin_type == self.cfg.OriginType.AUTO:
      self._set_camera_auto_track()
    elif self.cfg.origin_type == self.cfg.OriginType.WORLD:
      self._set_camera_world()
    elif self.cfg.origin_type == self.cfg.OriginType.ASSET_ROOT:
      self._set_camera_asset_root()
    else:  # ASSET_BODY
      self._set_camera_asset_body()

    self._camera.lookat = getattr(self.cfg, "lookat", self._camera.lookat)
    self._camera.elevation = getattr(self.cfg, "elevation", self._camera.elevation)
    self._camera.azimuth = getattr(self.cfg, "azimuth", self._camera.azimuth)
    self._camera.distance = getattr(self.cfg, "distance", self._camera.distance)

  def _set_camera_auto_track(self) -> None:
    """Track first non-fixed body; fall back to free camera if none exists."""
    assert self.mjm is not None
    for body_id in range(self.mjm.nbody):
      is_weld = self.mjm.body_weldid[body_id] == 0
      root_id = self.mjm.body_rootid[body_id]
      root_is_mocap = self.mjm.body_mocapid[root_id] >= 0
      if not (is_weld and not root_is_mocap):
        self._track_body(body_id)
        return
    self._set_camera_world()

  def _set_camera_world(self) -> None:
    """Configure free camera in world frame."""
    self._camera.type = mujoco.mjtCamera.mjCAMERA_FREE.value
    self._camera.fixedcamid = -1
    self._camera.trackbodyid = -1

  def _track_body(self, body_id: int) -> None:
    self._camera.type = mujoco.mjtCamera.mjCAMERA_TRACKING.value
    self._camera.trackbodyid = body_id
    self._camera.fixedcamid = -1

  def _set_camera_asset_root(self) -> None:
    """Track the root body of a configured asset."""
    if not self.cfg.entity_name:
      raise ValueError("Asset name must be specified for ASSET_ROOT origin type")
    robot: Entity = self.env.unwrapped.scene[self.cfg.entity_name]
    self._track_body(robot.indexing.root_body_id)

  def _set_camera_asset_body(self) -> None:
    """Track a specific body of a configured asset."""
    if not self.cfg.entity_name or not self.cfg.body_name:
      raise ValueError("entity_name/body_name required for ASSET_BODY origin type")
    robot: Entity = self.env.unwrapped.scene[self.cfg.entity_name]
    if self.cfg.body_name not in robot.body_names:
      raise ValueError(
        f"Body '{self.cfg.body_name}' not found in asset '{self.cfg.entity_name}'"
      )
    body_id_list, _ = robot.find_bodies(self.cfg.body_name)
    self._track_body(robot.indexing.bodies[body_id_list[0]].id)

  def _init_reward_plots(self, term_names: list[str]) -> None:
    """Create per-term histories."""
    self._histories = {
      name: deque(maxlen=self._plot_cfg.history) for name in term_names
    }

  def _clear_histories(self) -> None:
    for history in self._histories.values():
      history.clear()
