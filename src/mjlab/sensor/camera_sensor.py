"""Camera sensor for RGB, depth, and segmentation rendering."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

import mujoco
import mujoco_warp as mjwarp
import torch

from mjlab.entity import Entity
from mjlab.sensor.sensor import Sensor, SensorCfg

if TYPE_CHECKING:
  from mjlab.sensor.sensor_context import SensorContext

CameraDataType = Literal["rgb", "depth", "segmentation"]

# Default MuJoCo fov, in degrees.
_DEFAULT_CAM_FOVY = 45.0


@dataclass
class CameraSensorCfg(SensorCfg):
  """Configuration for a camera sensor.

  A camera sensor can either wrap an existing MuJoCo camera
  (``camera_name``) or create a new one at the specified
  pos/quat. New cameras are added to the worldbody by default,
  or to a specific body via ``parent_body``.

  Note:
    All camera sensors in a scene must share identical values for
    use_textures, use_shadows, and enabled_geom_groups. This is a
    constraint of the underlying mujoco_warp rendering system.
  """

  camera_name: str | None = None
  """Name of an existing MuJoCo camera to wrap.

  If None, a new camera is created using pos/quat/fovy.
  If set, the sensor wraps the named camera instead of creating one.
  """

  parent_body: str | None = None
  """Parent body to attach a new camera to.

  Only used when ``camera_name`` is None (creating a new camera).
  If None, the camera is added to the worldbody. Use the full
  prefixed name (e.g., "robot/link_6") to attach to an entity's
  body. The pos/quat are then relative to the parent body frame.
  """

  pos: tuple[float, float, float] = (0.0, 0.0, 1.0)
  """Camera position (used when creating a new camera).

  World-frame if parent_body is None, otherwise relative to the
  parent body frame.
  """

  quat: tuple[float, float, float, float] = (1.0, 0.0, 0.0, 0.0)
  """Camera orientation quaternion (w, x, y, z)."""

  fovy: float | None = None
  """Vertical field of view in degrees. None uses MuJoCo default."""

  width: int = 160
  """Image width in pixels."""

  height: int = 120
  """Image height in pixels."""

  data_types: tuple[CameraDataType, ...] = ("rgb",)
  """Data types to capture: any combination of "rgb", "depth",
  and "segmentation"."""

  use_textures: bool = True
  """Whether to use textures in rendering."""

  use_shadows: bool = False
  """Whether to use shadows in rendering."""

  enabled_geom_groups: tuple[int, ...] = (0, 1, 2)
  """Geom groups (0-5) visible to the camera."""

  orthographic: bool = False
  """Use orthographic projection instead of perspective."""

  fps: float | None = None
  """Camera frame rate in Hz.

  If None, a new frame is surfaced every time the scene is sensed (once per
  control step). If set, the sensor refreshes its output only once every
  ``1 / fps`` seconds of simulated time and holds the last frame in between,
  like a real camera that is slower than the control loop. All data types of
  the camera refresh together so they always come from the same instant.

  Each environment starts with a random phase so frames do not refresh in
  lockstep across environments. Reset environments receive a fresh frame on
  the next sense. Rates at or above the control rate produce a fresh frame
  every step, i.e. behave like None. The effective rate is quantized to
  control steps.

  Note:
    On its own this does not reduce rendering cost. Frames are still rendered
    every step; the ones between refreshes are simply not surfaced. See
    ``phase`` for how to skip renders.
  """

  phase: Literal["random", "aligned"] = "random"
  """How frame refreshes are timed across environments when ``fps`` is set.

  ``"random"`` gives each environment its own phase so refreshes are
  staggered, like a fleet of unsynchronized cameras. ``"aligned"`` refreshes
  every environment on the same control steps. When every camera in the scene
  is aligned, the simulation skips rendering on steps where no camera is due,
  cutting render cost by the ratio of the fastest camera's rate to the control
  rate. Steps on which an environment is reset always render so it starts
  with a fresh frame, so the saving shrinks as resets become more frequent.
  Ignored when ``fps`` is None.
  """

  clone_data: bool = False
  """If True, clone tensors on each access.

  Set to True if you modify the returned data in-place.
  """

  def __post_init__(self) -> None:
    valid = {"rgb", "depth", "segmentation"}
    invalid = {dt for dt in self.data_types if dt not in valid}
    if invalid:
      raise ValueError(f"Invalid camera data types: {invalid}. Valid types: {valid}")
    if not self.data_types:
      raise ValueError("At least one data type must be specified.")
    if self.fps is not None and self.fps <= 0:
      raise ValueError(f"fps must be positive, got {self.fps}.")
    if self.phase not in ("random", "aligned"):
      raise ValueError(f"phase must be 'random' or 'aligned', got {self.phase!r}.")

  def build(self) -> CameraSensor:
    return CameraSensor(self)


@dataclass
class CameraSensorData:
  """Camera sensor output data.

  Shapes:
    - rgb: [num_envs, height, width, 3] (uint8)
    - depth: [num_envs, height, width, 1] (float32)
    - segmentation: [num_envs, height, width, 2] (int32)
  """

  rgb: torch.Tensor | None = None
  """RGB image [num_envs, height, width, 3] (uint8). None if not
  enabled."""

  depth: torch.Tensor | None = None
  """Depth image [num_envs, height, width, 1] (float32). None if not
  enabled."""

  segmentation: torch.Tensor | None = None
  """Per-pixel typed segmentation [num_envs, height, width, 2] (int32).

  Channel 0 stores MuJoCo object IDs. Channel 1 stores the corresponding
  MuJoCo object types. Background pixels are ``(-1, -1)``.
  """


# Tolerance when comparing accumulated simulated time against the frame period,
# so float accumulation error never skips a frame that is due.
_FRAME_TIME_EPS = 1e-6


class CameraSensor(Sensor[CameraSensorData]):
  """Camera sensor for RGB and depth rendering."""

  requires_sensor_context = True

  def __init__(self, cfg: CameraSensorCfg) -> None:
    super().__init__()
    self.cfg = cfg
    self._camera_name = cfg.camera_name if cfg.camera_name is not None else cfg.name
    self._is_wrapping_existing = cfg.camera_name is not None
    self._ctx: SensorContext | None = None
    self._camera_idx: int = -1
    # Frame-rate state. Only used when ``cfg.fps`` is set.
    self._period: float | None = None if cfg.fps is None else 1.0 / cfg.fps
    self._pending_dt: float = 0.0
    self._held: dict[CameraDataType, torch.Tensor] = {}
    # Random phase: per-env time since the last refresh.
    self._elapsed: torch.Tensor | None = None
    # Aligned phase: one host-side clock shared by all envs, plus the envs reset
    # since time last advanced, which must refresh regardless of the clock.
    self._clock: float = 0.0
    self._force: torch.Tensor | None = None
    self._force_pending: bool = False

  @property
  def camera_name(self) -> str:
    return self._camera_name

  @property
  def camera_idx(self) -> int:
    return self._camera_idx

  @property
  def aligned(self) -> bool:
    """Whether all envs refresh on the same senses (``fps`` set, aligned phase)."""
    return self._period is not None and self.cfg.phase == "aligned"

  @property
  def needs_render(self) -> bool:
    """Whether the next sense must render for this camera to be correct.

    Always True unless the camera is aligned, in which case it is True only
    when the shared clock will cross the frame period on the next sense or an
    env was reset since simulated time last advanced. Evaluate before
    :meth:`capture`.
    """
    if not self.aligned:
      return True
    assert self._period is not None
    if self._force_pending:
      return True
    return self._clock + self._pending_dt >= self._period - _FRAME_TIME_EPS

  def edit_spec(
    self,
    scene_spec: mujoco.MjSpec,
    entities: dict[str, Entity],
  ) -> None:
    del entities

    if self._is_wrapping_existing:
      cam = scene_spec.camera(self._camera_name)
      assert isinstance(cam, mujoco.MjsCamera)
      if self.cfg.fovy is not None:
        cam.fovy = self.cfg.fovy
      if self.cfg.orthographic:
        cam.proj = mujoco.mjtProjection.mjPROJ_ORTHOGRAPHIC
      return

    if self.cfg.parent_body is not None:
      parent = scene_spec.body(self.cfg.parent_body)
    else:
      parent = scene_spec.worldbody

    proj = (
      mujoco.mjtProjection.mjPROJ_ORTHOGRAPHIC
      if self.cfg.orthographic
      else mujoco.mjtProjection.mjPROJ_PERSPECTIVE
    )
    parent.add_camera(
      name=self.cfg.name,
      pos=self.cfg.pos,
      quat=self.cfg.quat,
      fovy=self.cfg.fovy if self.cfg.fovy is not None else _DEFAULT_CAM_FOVY,
      resolution=[self.cfg.width, self.cfg.height],
      proj=proj,
    )

  def initialize(
    self,
    mj_model: mujoco.MjModel,
    model: mjwarp.Model,
    data: mjwarp.Data,
    device: str,
  ) -> None:
    del model

    try:
      cam = mj_model.camera(self._camera_name)
      self._camera_idx = cam.id
    except KeyError as e:
      available = [mj_model.camera(i).name for i in range(mj_model.ncam)]
      raise ValueError(
        f"Camera '{self._camera_name}' not found in model. Available: {available}"
      ) from e

    if self._period is None:
      return
    if self.aligned:
      # Due on the first sense; all envs share the clock afterwards.
      self._clock = self._period
      self._force = torch.zeros(data.nworld, dtype=torch.bool, device=device)
      return
    self._elapsed = torch.zeros(data.nworld, dtype=torch.float64, device=device)
    self._arm(slice(None))

  def set_context(self, ctx: SensorContext) -> None:
    self._ctx = ctx
    if self._period is None:
      return
    self._held = {
      data_type: torch.zeros_like(self._render_output(data_type))
      for data_type in self.cfg.data_types
    }

  def reset(self, env_ids: torch.Tensor | slice | None = None) -> None:
    super().reset(env_ids)
    if self._period is None:
      return
    if env_ids is None:
      env_ids = slice(None)
    if self._force is not None:
      # Aligned: refresh on the next sense but keep the shared clock.
      self._force[env_ids] = True
      self._force_pending = True
      return
    self._arm(env_ids)

  def _arm(self, env_ids: torch.Tensor | slice) -> None:
    """Make ``env_ids`` due now, with a fresh random phase once time advances.

    Used at initialization and on reset so an env never starts an episode
    holding a stale frame, while refreshes stay staggered across envs.
    """
    assert self._elapsed is not None and self._period is not None
    n = self._elapsed[env_ids].shape[0]
    phase = torch.rand(n, dtype=torch.float64, device=self._elapsed.device)
    self._elapsed[env_ids] = (1.0 + phase) * self._period

  def update(self, dt: float) -> None:
    super().update(dt)
    self._pending_dt += dt

  def capture(self, rendered: bool = True) -> None:
    """Take the freshly rendered frame into the surfaced output.

    Called by :class:`SensorContext` after every sense. Without ``fps`` this
    only invalidates the cache so reads see the new render. With ``fps`` it
    copies the render into the held frame for environments whose frame period
    has elapsed and leaves the others untouched. The period is only consumed
    once simulated time has advanced, so an env stays due across repeated
    senses at the same instant (e.g. a reset followed by a state edit).

    Args:
      rendered: Whether this sense rendered. May only be False when
        :attr:`needs_render` was False before the sense; the clock still
        advances so the next due step is computed correctly.
    """
    self._invalidate_cache()
    if self._period is None:
      return
    if self.aligned:
      self._capture_aligned(rendered)
      return
    assert rendered, "Random-phase cameras need a render on every sense."
    assert self._elapsed is not None
    self._elapsed += self._pending_dt
    due = self._elapsed >= self._period - _FRAME_TIME_EPS
    self._refresh(due)
    if self._pending_dt == 0.0:
      return
    self._pending_dt = 0.0
    # Keep the sub-period remainder so each env's phase is preserved. Subtract
    # the period before taking the remainder so a clock within the tolerance
    # just below the period is consumed rather than left due again.
    remainder = torch.remainder(
      torch.clamp(self._elapsed - self._period, min=0.0), self._period
    )
    self._elapsed = torch.where(due, remainder, self._elapsed)

  def _capture_aligned(self, rendered: bool) -> None:
    assert self._period is not None and self._force is not None
    self._clock += self._pending_dt
    due = self._clock >= self._period - _FRAME_TIME_EPS
    if not rendered:
      assert not due and not self._force_pending, (
        "Sense skipped rendering while an aligned camera was due."
      )
      self._pending_dt = 0.0
      return
    if due:
      for data_type, held in self._held.items():
        held.copy_(self._render_output(data_type))
    elif self._force_pending:
      self._refresh(self._force)
    if self._pending_dt == 0.0:
      return
    self._pending_dt = 0.0
    if due:
      # Same boundary handling as the per-env clock above.
      self._clock = max(self._clock - self._period, 0.0) % self._period
    if self._force_pending:
      self._force.zero_()
      self._force_pending = False

  def _refresh(self, mask: torch.Tensor) -> None:
    """Copy the latest render into the held frames of envs in ``mask``."""
    env_mask = mask.view(-1, 1, 1, 1)
    for data_type, held in self._held.items():
      fresh = self._render_output(data_type)
      held.copy_(torch.where(env_mask, fresh, held))

  def _render_output(self, data_type: CameraDataType) -> torch.Tensor:
    """View of the latest render for ``data_type`` (zero-copy)."""
    if self._ctx is None:
      raise RuntimeError(
        "CameraSensor requires a SensorContext. "
        "Ensure the sensor is part of a scene with "
        "sim.sense() calls."
      )
    if data_type == "rgb":
      return self._ctx.get_rgb(self._camera_idx)
    if data_type == "depth":
      return self._ctx.get_depth(self._camera_idx)
    return self._ctx.get_segmentation(self._camera_idx)

  def _output(self, data_type: CameraDataType) -> torch.Tensor | None:
    if data_type not in self.cfg.data_types:
      return None
    if self._period is None:
      fresh = self._render_output(data_type)
      return fresh.clone() if self.cfg.clone_data else fresh
    held = self._held[data_type]
    return held.clone() if self.cfg.clone_data else held

  def _compute_data(self) -> CameraSensorData:
    return CameraSensorData(
      rgb=self._output("rgb"),
      depth=self._output("depth"),
      segmentation=self._output("segmentation"),
    )
