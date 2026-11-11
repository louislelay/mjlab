"""MuJoCo Studio plugins and messages backing the native viewer.

MuJoCo Studio runs its window on a separate viewer thread that owns a private
copy of ``MjModel`` and ``MjData``. ``ViewerHandle.sync`` only forwards the
integration state, so everything else the native viewer shows (overlay geoms,
neighbouring environments, domain randomized visual fields, status text and
reward plots) travels in a :class:`FrameSnapshot`. In the other direction,
key presses and the mouse perturbation travel back to the simulation thread as
:class:`KeyEvent` and :class:`MousePerturbSnapshot`.
"""

from __future__ import annotations

import copy
import dataclasses
import sys

import mujoco
import numpy as np
from mujoco.studio import app as studio_app
from mujoco.studio import launch_passive, messages, plugin, ux, viewer_protocol
from mujoco.studio.app import inputs
from mujoco.studio.dear_imgui import dear_imgui as imgui
from mujoco.studio.implot import implot

from mjlab.viewer.native import keys

_KEY_NAMES = {
  "SPACE": "Space",
  "APOSTROPHE": "Apostrophe",
  "COMMA": "Comma",
  "MINUS": "Minus",
  "PERIOD": "Period",
  "SLASH": "Slash",
  "SEMICOLON": "Semicolon",
  "EQUAL": "Equal",
  "LEFT_BRACKET": "LeftBracket",
  "BACKSLASH": "Backslash",
  "RIGHT_BRACKET": "RightBracket",
  "GRAVE_ACCENT": "GraveAccent",
  "ESCAPE": "Escape",
  "ENTER": "Enter",
  "TAB": "Tab",
  "BACKSPACE": "Backspace",
  "INSERT": "Insert",
  "DELETE": "Delete",
  "RIGHT": "RightArrow",
  "LEFT": "LeftArrow",
  "DOWN": "DownArrow",
  "UP": "UpArrow",
}


def _imgui_key_name(suffix: str) -> str:
  if suffix in _KEY_NAMES:
    return _KEY_NAMES[suffix]
  if suffix.isdigit():
    return f"N{suffix}"
  return suffix


def _build_key_codes() -> dict[imgui.Key, int]:
  """Map Dear ImGui keys to the GLFW codes in :mod:`mjlab.viewer.native.keys`."""
  codes: dict[imgui.Key, int] = {}
  for name, code in vars(keys).items():
    if not name.startswith("KEY_") or code < 0:
      continue
    key = getattr(imgui.Key, _imgui_key_name(name.removeprefix("KEY_")), None)
    if key is not None:
      codes[key] = code
  return codes


KEY_CODES: dict[imgui.Key, int] = _build_key_codes()
"""Dear ImGui key to GLFW key code, so ``key_callback`` keeps its contract."""


@dataclasses.dataclass(frozen=True)
class RewardPlot:
  """History of one reward term, oldest sample first."""

  name: str
  values: np.ndarray


@dataclasses.dataclass(frozen=True, eq=False)
class FrameSnapshot(messages.Snapshot):
  """Per-frame visual state sent from the simulation to the viewer.

  Attributes:
    geoms: Decorative and neighbouring-environment geoms to draw.
    model_fields: Per-world model field values for the selected environment.
      Empty when no visual field is domain randomized.
    tracked_body: Body whose ``subtree_com`` is pinned to its frame origin so
      inertial randomization does not shift the tracking camera, or -1.
    status: Labels and values shown in the status overlay.
    plots: Reward term histories, empty when plots are hidden.
  """

  geoms: tuple[mujoco.MjvGeom, ...]
  model_fields: dict[str, np.ndarray]
  tracked_body: int
  status: tuple[str, str]
  plots: tuple[RewardPlot, ...]


@dataclasses.dataclass(frozen=True)
class KeyEvent(messages.Event):
  """A key press in the viewer window, as a GLFW key code."""

  key: int


@dataclasses.dataclass(frozen=True, eq=False)
class MousePerturbSnapshot(messages.Snapshot):
  """The viewer's mouse perturbation state."""

  perturb: mujoco.MjvPerturb


@dataclasses.dataclass(frozen=True)
class ViewerSettings:
  """Initial camera and rendering options for the Studio window.

  Attributes:
    camera: Initial camera.
    shadows: Whether to render shadows.
    enable_perturbations: Whether mouse picking and dragging perturb bodies.
  """

  camera: mujoco.MjvCamera
  shadows: bool
  enable_perturbations: bool


class MjlabViewerPlugin(plugin.ViewerPlugin):
  """Viewer-thread plugin: draws mjlab overlays and forwards user input."""

  def __init__(self, settings: ViewerSettings) -> None:
    self._settings = settings
    self._ux_state = ux.UxState()
    self._frame: FrameSnapshot | None = None
    self._fields_applied = True
    self._camera_initialized = False

  @messages.handler
  def on_post_model(self, _: messages.PostModelEvent) -> None:
    if self._camera_initialized:
      return
    self._camera_initialized = True
    for name in ("type", "trackbodyid", "fixedcamid", "elevation", "azimuth"):
      setattr(self.viewer.camera, name, getattr(self._settings.camera, name))
    self.viewer.camera.distance = self._settings.camera.distance
    self.viewer.camera.lookat[:] = self._settings.camera.lookat
    self.viewer.vis_options.frame = mujoco.mjtFrame.mjFRAME_WORLD.value
    self.viewer.vis_options.flags[mujoco.mjtVisFlag.mjVIS_SCLINERTIA] = 1
    shadow = mujoco.mjtRndFlag.mjRND_SHADOW
    self.viewer.render_flags.flags[shadow] = int(self._settings.shadows)

  @messages.handler
  def on_frame(self, frame: FrameSnapshot) -> None:
    self._frame = frame
    self._fields_applied = False

  @messages.handler
  def on_update(self, _: messages.UpdateEvent) -> None:
    self._handle_input()
    frame = self._frame
    if frame is None:
      return
    model, data = self.viewer.model, self.viewer.data
    if not self._fields_applied and frame.model_fields:
      for name, value in frame.model_fields.items():
        getattr(model, name)[:] = value
    self._fields_applied = True
    if frame.model_fields:
      mujoco.mj_forward(model, data)
    if 0 <= frame.tracked_body < model.nbody:
      data.subtree_com[frame.tracked_body] = data.xpos[frame.tracked_body]
    self.viewer.extra_geoms[:] = frame.geoms

  @messages.handler
  def on_build_gui(self, _: messages.BuildGuiEvent) -> None:
    frame = self._frame
    if frame is None:
      return
    self._build_status_gui(frame.status)
    if frame.plots:
      self._build_plots_gui(frame.plots)

  def _handle_input(self) -> None:
    io = imgui.GetIO()
    if not io.WantCaptureKeyboard:
      for key, code in KEY_CODES.items():
        if imgui.IsKeyPressed(key, repeat=False):
          self.viewer.send_to_sim(KeyEvent(key=code))

    perturb = self.viewer.perturb
    if not self._settings.enable_perturbations:
      perturb.select = 0
    inputs.handle_mouse_events(
      self.viewer.model,
      self.viewer.data,
      self.viewer.camera,
      self.viewer.vis_options,
      perturb,
      self._ux_state,
    )
    if not self._settings.enable_perturbations:
      perturb.select = 0
      perturb.active = 0
    self.viewer.send_to_sim(MousePerturbSnapshot(perturb=copy.deepcopy(perturb)))

  @staticmethod
  def _build_status_gui(status: tuple[str, str]) -> None:
    imgui.SetNextWindowPos(imgui.Vec2(10.0, 10.0), imgui.Cond.FirstUseEver)
    imgui.SetNextWindowBgAlpha(0.5)
    flags = (
      int(imgui.WindowFlags.NoDecoration)
      | int(imgui.WindowFlags.AlwaysAutoResize)
      | int(imgui.WindowFlags.NoFocusOnAppearing)
      | int(imgui.WindowFlags.NoNav)
    )
    visible, _ = imgui.Begin("mjlab status", flags=flags)
    if visible and imgui.BeginTable("status", 2):
      for label, value in zip(
        status[0].splitlines(), status[1].splitlines(), strict=False
      ):
        imgui.TableNextRow()
        imgui.TableNextColumn()
        imgui.TextUnformatted(label)
        imgui.TableNextColumn()
        imgui.TextUnformatted(value)
      imgui.EndTable()
    imgui.End()

  @staticmethod
  def _build_plots_gui(plots: tuple[RewardPlot, ...]) -> None:
    width = imgui.GetIO().DisplaySize.x
    imgui.SetNextWindowPos(
      imgui.Vec2(width - 10.0, 10.0), imgui.Cond.FirstUseEver, imgui.Vec2(1.0, 0.0)
    )
    imgui.SetNextWindowSize(imgui.Vec2(360.0, 600.0), imgui.Cond.FirstUseEver)
    imgui.SetNextWindowBgAlpha(0.5)
    visible, _ = imgui.Begin("Reward terms")
    if visible:
      fit = int(implot.AxisFlags.AutoFit)
      for plot in plots:
        if implot.BeginPlot(f"{plot.name}##reward", imgui.Vec2(-1.0, 150.0)):
          implot.SetupAxes("", "", fit, fit)
          xs = np.arange(-len(plot.values) + 1, 1, dtype=np.float64)
          implot.PlotLine(plot.name, xs.tolist(), plot.values.tolist())
          implot.EndPlot()
    imgui.End()


class MjlabSimPlugin(plugin.SimPlugin):
  """Simulation-thread plugin: collects input forwarded by the viewer.

  ``ViewerHandle.sync`` dispatches viewer messages to this plugin on the
  calling thread, so the viewer can read them right after each sync.
  """

  def __init__(self) -> None:
    self.perturb = mujoco.MjvPerturb()
    self.keys: list[int] = []

  @messages.handler
  def on_key(self, event: KeyEvent) -> None:
    self.keys.append(event.key)

  @messages.handler
  def on_perturb(self, snapshot: MousePerturbSnapshot) -> None:
    self.perturb = snapshot.perturb

  def pop_keys(self) -> list[int]:
    """Return and clear the key presses received since the last call."""
    pressed, self.keys = self.keys, []
    return pressed


def default_gfx() -> str:
  """MuJoCo Studio graphics mode: the web viewer on macOS, else a window.

  On macOS, Studio cannot open a desktop window from Python: AppKit requires
  windows on the main thread, while Studio runs its viewer on a background
  thread.
  """
  return "web" if sys.platform == "darwin" else ""


def view_model(
  model: mujoco.MjModel, title: str = "mjlab", gfx: str | None = None
) -> None:
  """Open ``model`` in the MuJoCo Studio app and simulate it on the CPU.

  Blocks until the viewer is closed.

  Args:
    model: Compiled model to show.
    title: Window title.
    gfx: Studio graphics mode. Defaults to :func:`default_gfx`.
  """
  gfx = default_gfx() if gfx is None else gfx
  launch_passive.run(
    viewer_protocol.ViewerConfig(title=title, gfx=gfx, open_browser=gfx == "web"),
    model=model,
    plugins=[studio_app.App(), *studio_app.SIM_PLUGINS],
  )
