"""
MuJoCo platform UX components.
"""
from __future__ import annotations
import collections.abc
import mujoco._specs
import mujoco._structs
import mujoco.studio._studio.sim
import mujoco.studio._studio.ux
import typing
__all__: list[str] = ['CameraMotion', 'ConsoleCounts', 'FREE_CAMERA_IDX', 'GuiTheme', 'InitPerturb', 'MIN_FLY_SPEED', 'MoveCamera', 'MovePerturb', 'ORBIT', 'PAN_TILT', 'PLANAR_MOVE_H', 'PLANAR_MOVE_V', 'Pick', 'PickResult', 'PipSource', 'PipState', 'RenderFlags', 'TRACKING_CAMERA_IDX', 'TRUCK_DOLLY', 'TRUCK_PEDESTAL', 'TUMBLE_CAMERA_IDX', 'UxState', 'ZOOM', 'add_console_message', 'camera_selection_gui', 'camera_to_string', 'clear_console', 'configure_docking_layout', 'console_gui', 'console_status_gui', 'controls_gui', 'convergence_gui', 'counts_gui', 'frame_selection_gui', 'get_console_counts', 'get_console_lines', 'get_default_ini_path', 'groups_gui', 'info_gui', 'init_console', 'joints_gui', 'label_selection_gui', 'load_history_frame', 'load_settings', 'load_theme', 'move_camera_with_keys', 'move_camera_with_mouse', 'noise_gui', 'physics_gui', 'pip_gui', 'record_history', 'rendering_gui', 'reset_config', 'reset_history', 'save_settings', 'sensor_gui', 'set_camera', 'set_imgui_context', 'set_implot_context', 'set_speed_index', 'setup_theme', 'simulation_gui', 'state_gui', 'step_control_gui', 'theme_menu_gui', 'theme_select_gui', 'timeline_scrubber_gui', 'unwind_imgui_frame', 'view_gizmo_gui', 'visualization_gui', 'watch_gui']
class CameraMotion:
    """
    Members:
    
      ZOOM
    
      ORBIT
    
      TRUCK_PEDESTAL
    
      TRUCK_DOLLY
    
      PAN_TILT
    
      PLANAR_MOVE_H
    
      PLANAR_MOVE_V
    """
    ORBIT: typing.ClassVar[mujoco.studio._studio.ux.CameraMotion]  # value = <CameraMotion.ORBIT: 1>
    PAN_TILT: typing.ClassVar[mujoco.studio._studio.ux.CameraMotion]  # value = <CameraMotion.PAN_TILT: 4>
    PLANAR_MOVE_H: typing.ClassVar[mujoco.studio._studio.ux.CameraMotion]  # value = <CameraMotion.PLANAR_MOVE_H: 5>
    PLANAR_MOVE_V: typing.ClassVar[mujoco.studio._studio.ux.CameraMotion]  # value = <CameraMotion.PLANAR_MOVE_V: 6>
    TRUCK_DOLLY: typing.ClassVar[mujoco.studio._studio.ux.CameraMotion]  # value = <CameraMotion.TRUCK_DOLLY: 3>
    TRUCK_PEDESTAL: typing.ClassVar[mujoco.studio._studio.ux.CameraMotion]  # value = <CameraMotion.TRUCK_PEDESTAL: 2>
    ZOOM: typing.ClassVar[mujoco.studio._studio.ux.CameraMotion]  # value = <CameraMotion.ZOOM: 0>
    __members__: typing.ClassVar[dict[str, mujoco.studio._studio.ux.CameraMotion]]  # value = {'ZOOM': <CameraMotion.ZOOM: 0>, 'ORBIT': <CameraMotion.ORBIT: 1>, 'TRUCK_PEDESTAL': <CameraMotion.TRUCK_PEDESTAL: 2>, 'TRUCK_DOLLY': <CameraMotion.TRUCK_DOLLY: 3>, 'PAN_TILT': <CameraMotion.PAN_TILT: 4>, 'PLANAR_MOVE_H': <CameraMotion.PLANAR_MOVE_H: 5>, 'PLANAR_MOVE_V': <CameraMotion.PLANAR_MOVE_V: 6>}
    @typing.overload
    def __eq__(self: mujoco.studio._studio.ux.CameraMotion, other: mujoco.studio._studio.ux.CameraMotion) -> bool:
        ...
    @typing.overload
    def __eq__(self: mujoco.studio._studio.ux.CameraMotion, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self: mujoco.studio._studio.ux.CameraMotion) -> int:
        ...
    def __init__(self: mujoco.studio._studio.ux.CameraMotion, value: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __int__(self: mujoco.studio._studio.ux.CameraMotion) -> int:
        ...
    @typing.overload
    def __ne__(self: mujoco.studio._studio.ux.CameraMotion, other: mujoco.studio._studio.ux.CameraMotion) -> bool:
        ...
    @typing.overload
    def __ne__(self: mujoco.studio._studio.ux.CameraMotion, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self: mujoco.studio._studio.ux.CameraMotion, state: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ConsoleCounts:
    @property
    def errors(self) -> int:
        ...
    @property
    def messages(self) -> int:
        ...
    @property
    def warnings(self) -> int:
        ...
class GuiTheme:
    """
    Members:
    
      LIGHT
    
      DARK
    
      CLASSIC
    """
    CLASSIC: typing.ClassVar[mujoco.studio._studio.ux.GuiTheme]  # value = <GuiTheme.CLASSIC: 2>
    DARK: typing.ClassVar[mujoco.studio._studio.ux.GuiTheme]  # value = <GuiTheme.DARK: 1>
    LIGHT: typing.ClassVar[mujoco.studio._studio.ux.GuiTheme]  # value = <GuiTheme.LIGHT: 0>
    __members__: typing.ClassVar[dict[str, mujoco.studio._studio.ux.GuiTheme]]  # value = {'LIGHT': <GuiTheme.LIGHT: 0>, 'DARK': <GuiTheme.DARK: 1>, 'CLASSIC': <GuiTheme.CLASSIC: 2>}
    @typing.overload
    def __eq__(self: mujoco.studio._studio.ux.GuiTheme, other: mujoco.studio._studio.ux.GuiTheme) -> bool:
        ...
    @typing.overload
    def __eq__(self: mujoco.studio._studio.ux.GuiTheme, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self: mujoco.studio._studio.ux.GuiTheme) -> int:
        ...
    def __init__(self: mujoco.studio._studio.ux.GuiTheme, value: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __int__(self: mujoco.studio._studio.ux.GuiTheme) -> int:
        ...
    @typing.overload
    def __ne__(self: mujoco.studio._studio.ux.GuiTheme, other: mujoco.studio._studio.ux.GuiTheme) -> bool:
        ...
    @typing.overload
    def __ne__(self: mujoco.studio._studio.ux.GuiTheme, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self: mujoco.studio._studio.ux.GuiTheme, state: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class PickResult:
    @property
    def body(self) -> int:
        ...
    @body.setter
    def body(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def dist(self) -> float:
        ...
    @dist.setter
    def dist(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def flex(self) -> int:
        ...
    @flex.setter
    def flex(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def geom(self) -> int:
        ...
    @geom.setter
    def geom(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def point(self) -> tuple[float, float, float]:
        ...
    @point.setter
    def point(self, arg1: tuple) -> None:
        ...
    @property
    def skin(self) -> int:
        ...
    @skin.setter
    def skin(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
class PipSource:
    name: str
    def __init__(self: mujoco.studio._studio.ux.PipSource, name: str = '', texture: typing.SupportsInt | typing.SupportsIndex = 0, aspect_ratio: typing.SupportsFloat | typing.SupportsIndex = 1.0) -> None:
        ...
    @property
    def aspect_ratio(self) -> float:
        ...
    @aspect_ratio.setter
    def aspect_ratio(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def texture(self) -> int:
        ...
    @texture.setter
    def texture(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
class PipState:
    def __init__(self: mujoco.studio._studio.ux.PipState) -> None:
        ...
    @property
    def camera(self) -> int:
        ...
    @camera.setter
    def camera(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def texture(self) -> int:
        ...
    @texture.setter
    def texture(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
class RenderFlags:
    def __init__(self: mujoco.studio._studio.ux.RenderFlags) -> None:
        ...
    @property
    def flags(self) -> typing.Annotated[list[int], "FixedSize(12)"]:
        ...
    @flags.setter
    def flags(self, arg0: typing.Annotated[collections.abc.Sequence[typing.SupportsInt | typing.SupportsIndex], "FixedSize(12)"]) -> None:
        ...
class UxState:
    update_threadpool: bool
    watch_field_name: str
    def __init__(self: mujoco.studio._studio.ux.UxState) -> None:
        ...
    @property
    def camera_index(self) -> int:
        ...
    @camera_index.setter
    def camera_index(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def history_index(self) -> int:
        ...
    @history_index.setter
    def history_index(self, arg1: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def history_size(self) -> int:
        ...
    @history_size.setter
    def history_size(self, arg1: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def key_idx(self) -> int:
        ...
    @key_idx.setter
    def key_idx(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def nthread(self) -> int:
        ...
    @nthread.setter
    def nthread(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def sim_head_time(self) -> float:
        ...
    @sim_head_time.setter
    def sim_head_time(self, arg1: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def speed_index(self) -> int:
        ...
    @speed_index.setter
    def speed_index(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def state(self) -> list[float]:
        ...
    @state.setter
    def state(self, arg0: collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex]) -> None:
        ...
    @property
    def state_sig(self) -> int:
        ...
    @state_sig.setter
    def state_sig(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def watch_field_index(self) -> int:
        ...
    @watch_field_index.setter
    def watch_field_index(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
def InitPerturb(model: mujoco._structs.MjModel, data: mujoco._structs.MjData, cam: mujoco._structs.MjvCamera, pert: mujoco._structs.MjvPerturb, active: typing.SupportsInt | typing.SupportsIndex) -> None:
    """
    Initializes mouse perturbation.
    """
def MoveCamera(model: mujoco._structs.MjModel, data: mujoco._structs.MjData, cam: mujoco._structs.MjvCamera, motion: mujoco.studio._studio.ux.CameraMotion, dx: typing.SupportsFloat | typing.SupportsIndex, dy: typing.SupportsFloat | typing.SupportsIndex) -> None:
    """
    Moves the given camera.
    """
def MovePerturb(model: mujoco._structs.MjModel, data: mujoco._structs.MjData, cam: mujoco._structs.MjvCamera, pert: mujoco._structs.MjvPerturb, action: typing.SupportsInt | typing.SupportsIndex, reldx: typing.SupportsFloat | typing.SupportsIndex, reldy: typing.SupportsFloat | typing.SupportsIndex) -> None:
    """
    Moves mouse perturbation.
    """
def Pick(model: mujoco._structs.MjModel, data: mujoco._structs.MjData, cam: mujoco._structs.MjvCamera, x: typing.SupportsFloat | typing.SupportsIndex, y: typing.SupportsFloat | typing.SupportsIndex, aspect_ratio: typing.SupportsFloat | typing.SupportsIndex, opt: mujoco._structs.MjvOption) -> mujoco.studio._studio.ux.PickResult:
    """
    Picks object under cursor.
    """
def add_console_message(level: typing.SupportsInt | typing.SupportsIndex, message: str) -> None:
    """
    Adds a message at the given mjtLogLevel to the Studio Console (not printed).
    """
def camera_selection_gui(model: mujoco._structs.MjModel, data: mujoco._structs.MjData, camera: mujoco._structs.MjvCamera, ux_state: mujoco.studio._studio.ux.UxState) -> bool:
    """
    Render the camera selection GUI. Modifies ux_state.camera_index. Returns true if camera changed.
    """
def camera_to_string(data: mujoco._structs.MjData, camera: mujoco._structs.MjvCamera) -> str:
    """
    Returns an XML string representation of the camera.
    """
def clear_console() -> None:
    """
    Clears all messages and resets counts in the Studio Console.
    """
def configure_docking_layout(show_toolbar: bool = True, show_status_bar: bool = True) -> tuple[float, float, float, float]:
    """
    Configure the docking layout with Options (left) and Inspector (right) panes. Returns (x, y, w, h) of the central workspace area.
    """
def console_gui() -> None:
    """
    Renders the Studio Console table.
    """
def console_status_gui(show_console: bool) -> bool:
    """
    Renders the Studio Console status bar summary. Returns updated show_console state.
    """
def controls_gui(model: mujoco._structs.MjModel, data: mujoco._structs.MjData, vis_options: mujoco._structs.MjvOption) -> None:
    """
    Render the actuator controls UI.
    """
def convergence_gui(model: mujoco._structs.MjModel, data: mujoco._structs.MjData) -> None:
    """
    Render the solver convergence chart.
    """
def counts_gui(model: mujoco._structs.MjModel, data: mujoco._structs.MjData) -> None:
    """
    Render the solver counts chart.
    """
def frame_selection_gui(vis_options: mujoco._structs.MjvOption) -> bool:
    """
    Render the visualization frame selection GUI.
    """
def get_console_counts() -> mujoco.studio._studio.ux.ConsoleCounts:
    """
    Returns ConsoleCounts (messages, warnings, errors) for the Studio Console.
    """
def get_console_lines() -> list[str]:
    """
    Returns a list of log lines currently in the Studio Console. It copies every line, so call it on demand, e.g. in tests and scripts, rather than every frame.
    """
def get_default_ini_path() -> str:
    """
    Returns the default INI configuration file path (~/.mujoco.ini).
    """
def groups_gui(model: mujoco._structs.MjModel, vis_options: mujoco._structs.MjvOption, min_width: typing.SupportsFloat | typing.SupportsIndex = 150.0) -> None:
    """
    Render the visibility groups UI.
    """
def info_gui(model: mujoco._structs.MjModel, data: mujoco._structs.MjData, paused: bool, fps: typing.SupportsFloat | typing.SupportsIndex, gpu_ms: typing.SupportsFloat | typing.SupportsIndex = 0.0) -> None:
    """
    Render the simulation info UI.
    """
def init_console() -> None:
    """
    Installs a MuJoCo log handler that adds messages to the Studio Console and passes them on to the previous handler. Only the first call installs it.
    """
def joints_gui(model: mujoco._structs.MjModel, data: mujoco._structs.MjData, vis_options: mujoco._structs.MjvOption) -> None:
    """
    Render the joints UI.
    """
def label_selection_gui(vis_options: mujoco._structs.MjvOption) -> bool:
    """
    Render the visualization label selection GUI.
    """
def load_history_frame(history: mujoco.studio._studio.sim.SimHistory, model: typing.Any, data: typing.Any, index: typing.SupportsInt | typing.SupportsIndex) -> None:
    """
    Load the history frame at `index` (0 is the most recent state) into `data`. A no-op if the frame is empty.
    """
def load_settings(ini_path: str = '', def_theme: mujoco.studio._studio.ux.GuiTheme = ...) -> mujoco.studio._studio.ux.GuiTheme:
    """
    Loads settings and theme from an INI file into ImGui.
    """
def load_theme(ini_path: str = '', def_theme: mujoco.studio._studio.ux.GuiTheme = ...) -> mujoco.studio._studio.ux.GuiTheme:
    """
    Loads the GUI theme from an INI file.
    """
def move_camera_with_keys(model: mujoco._structs.MjModel, camera: mujoco._structs.MjvCamera, speed: typing.SupportsFloat | typing.SupportsIndex) -> tuple[bool, float]:
    """
    Flies the fly camera with this frame's ImGui WASD/QE keys as Studio does. Returns (moved, speed), with the fly speed for the next frame.
    """
def move_camera_with_mouse(model: mujoco._structs.MjModel, camera: mujoco._structs.MjvCamera, fly_camera: bool) -> bool:
    """
    Moves the camera with this frame's ImGui mouse drags and wheel as Studio maps them. Returns whether it moved.
    """
def noise_gui(step_control: mujoco.studio._studio.sim.StepControl) -> None:
    """
    Render the noise UI.
    """
def physics_gui(model: mujoco._structs.MjModel, spec: mujoco._specs.MjSpec = None, min_width: typing.SupportsFloat | typing.SupportsIndex = 150.0) -> None:
    """
    Render the physics settings UI.
    """
def pip_gui(sources: collections.abc.Sequence[mujoco.studio._studio.ux.PipSource], pips: collections.abc.Sequence[mujoco.studio._studio.ux.PipState]) -> list[mujoco.studio._studio.ux.PipState]:
    ...
def record_history(history: mujoco.studio._studio.sim.SimHistory, ux_state: mujoco.studio._studio.ux.UxState, model: typing.Any, data: typing.Any) -> None:
    """
    Append the current state to the history buffer and move the head of the timeline to it. Call whenever the simulation has advanced.
    """
def rendering_gui(model: mujoco._structs.MjModel, vis_options: mujoco._structs.MjvOption, render_flags: mujoco.studio._studio.ux.RenderFlags) -> None:
    """
    Render the rendering settings UI. Modifies render_flags in place.
    """
def reset_config(ini_path: str = '') -> None:
    """
    Resets the configuration INI file.
    """
def reset_history(history: mujoco.studio._studio.sim.SimHistory, ux_state: mujoco.studio._studio.ux.UxState, model: typing.Any, data: typing.Any) -> None:
    """
    (Re)initialize the history buffer for the model, reset the timeline and record the current state as the first frame. Call on model load and after a reset.
    """
def save_settings(theme: mujoco.studio._studio.ux.GuiTheme, ini_path: str = '') -> None:
    """
    Saves settings and theme to an INI file.
    """
def sensor_gui(model: mujoco._structs.MjModel, data: mujoco._structs.MjData) -> None:
    """
    Render the sensor data plot.
    """
def set_camera(model: mujoco._structs.MjModel, camera: mujoco._structs.MjvCamera, request_idx: typing.SupportsInt | typing.SupportsIndex) -> int:
    """
    Set the camera index and update the camera object.
    """
def set_imgui_context(ptr: typing.SupportsInt | typing.SupportsIndex) -> None:
    """
    Set ImGui context pointer.
    """
def set_implot_context(ptr: typing.SupportsInt | typing.SupportsIndex) -> None:
    """
    Set ImPlot context pointer.
    """
def set_speed_index(step_control: mujoco.studio._studio.sim.StepControl, speed_index: typing.SupportsInt | typing.SupportsIndex, request_idx: typing.SupportsInt | typing.SupportsIndex) -> int:
    """
    Set the simulation speed index. Returns new_speed_index.
    """
def setup_theme(theme: mujoco.studio._studio.ux.GuiTheme) -> None:
    """
    Set up Dear ImGui visual theme.
    """
def simulation_gui(model: typing.Any, data: typing.Any, step_control: mujoco.studio._studio.sim.StepControl, ux_state: mujoco.studio._studio.ux.UxState, reset: collections.abc.Callable, reload: collections.abc.Callable, align: collections.abc.Callable, save_keyframe: collections.abc.Callable) -> None:
    """
    Render the full Simulation panel: reset/reload/align, run/pause, speed, the history scrubber, keyframes and thread count. The four callbacks are invoked for the corresponding buttons.
    """
def state_gui(model: mujoco._structs.MjModel, data: mujoco._structs.MjData, ux_state: mujoco.studio._studio.ux.UxState, min_width: typing.SupportsFloat | typing.SupportsIndex = 150.0) -> None:
    """
    Render the state UI. Modifies ux_state.state and ux_state.state_sig.
    """
def step_control_gui(step_control: mujoco.studio._studio.sim.StepControl, ux_state: mujoco.studio._studio.ux.UxState) -> None:
    """
    Render the simulation stepping control GUI. Modifies ux_state.speed_index.
    """
def theme_menu_gui(theme: mujoco.studio._studio.ux.GuiTheme) -> tuple[bool, mujoco.studio._studio.ux.GuiTheme]:
    """
    Render the Theme menu. Returns (changed, theme).
    """
def theme_select_gui(theme: mujoco.studio._studio.ux.GuiTheme) -> tuple[bool, mujoco.studio._studio.ux.GuiTheme]:
    """
    Render the GUI theme selector. Returns (changed, theme).
    """
def timeline_scrubber_gui(model: typing.Any, data: typing.Any, step_control: mujoco.studio._studio.sim.StepControl, ux_state: mujoco.studio._studio.ux.UxState) -> None:
    """
    Render the timeline scrubber widget (spine + draggable knob).
    """
def unwind_imgui_frame() -> bool:
    """
    Unwinds every ImGui and ImPlot Begin*/Push* left open since NewFrame() without asserting; returns whether a frame was in progress.
    """
def view_gizmo_gui(model: mujoco._structs.MjModel, data: mujoco._structs.MjData, camera: mujoco._structs.MjvCamera, ux_state: mujoco.studio._studio.ux.UxState, workspace_rect: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(4)"]) -> bool:
    """
    Renders the XYZ view gizmo in workspace_rect, the (x, y, w, h) from configure_docking_layout. May modify ux_state.camera_index. Returns true if the camera changed.
    """
def visualization_gui(model: mujoco._structs.MjModel, vis_options: mujoco._structs.MjvOption, camera: mujoco._structs.MjvCamera, min_width: typing.SupportsFloat | typing.SupportsIndex = 150.0) -> None:
    """
    Render the visualization settings UI.
    """
def watch_gui(model: mujoco._structs.MjModel, data: mujoco._structs.MjData, ux_state: mujoco.studio._studio.ux.UxState) -> None:
    """
    Render the watch UI. Modifies ux_state.watch_field_name and ux_state.watch_field_index.
    """
FREE_CAMERA_IDX: int = -2
MIN_FLY_SPEED: float = 0.0010000000474974513
ORBIT: mujoco.studio._studio.ux.CameraMotion  # value = <CameraMotion.ORBIT: 1>
PAN_TILT: mujoco.studio._studio.ux.CameraMotion  # value = <CameraMotion.PAN_TILT: 4>
PLANAR_MOVE_H: mujoco.studio._studio.ux.CameraMotion  # value = <CameraMotion.PLANAR_MOVE_H: 5>
PLANAR_MOVE_V: mujoco.studio._studio.ux.CameraMotion  # value = <CameraMotion.PLANAR_MOVE_V: 6>
TRACKING_CAMERA_IDX: int = -1
TRUCK_DOLLY: mujoco.studio._studio.ux.CameraMotion  # value = <CameraMotion.TRUCK_DOLLY: 3>
TRUCK_PEDESTAL: mujoco.studio._studio.ux.CameraMotion  # value = <CameraMotion.TRUCK_PEDESTAL: 2>
TUMBLE_CAMERA_IDX: int = -3
ZOOM: mujoco.studio._studio.ux.CameraMotion  # value = <CameraMotion.ZOOM: 0>
