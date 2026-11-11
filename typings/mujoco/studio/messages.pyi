import contextlib
import dataclasses
import enum
import mujoco
import numpy as np
from _typeshed import Incomplete
from collections.abc import Iterator
from mujoco.studio import sim as sim
from typing import Any, Callable, Protocol

KEYFRAME_STATE_SIG: Incomplete

class Message: ...
class Snapshot(Message): ...
class Event(Message): ...

class SnapshotChannel(Protocol):
    def put(self, value: Snapshot) -> None: ...
    def get(self) -> list[Snapshot]: ...
    def reclaim_unconsumed(self, snapshot_type: type[Snapshot]) -> Snapshot | None: ...
    def close(self) -> None: ...

class EventChannel(Protocol):
    def put(self, value: Event) -> None: ...
    def get(self) -> list[Event]: ...
    def close(self) -> None: ...
MakeMessage = Callable[[], Message | None]

@contextlib.contextmanager
def send_if_changes(send_fn: Callable[[Message], None], *make_messages: MakeMessage, should_send: Callable[[], bool] | None = None) -> Iterator[None]: ...

@dataclasses.dataclass(frozen=True, eq=False)
class StateSnapshot(Snapshot):
    state: np.ndarray
    state_sig: int
    def __eq__(self, other: object) -> bool: ...

@dataclasses.dataclass(frozen=True, eq=False)
class PerturbSnapshot(Snapshot):
    state: np.ndarray
    state_sig: int
    def __eq__(self, other: object) -> bool: ...

@dataclasses.dataclass(frozen=True, eq=False)
class StateEvent(Event):
    state: np.ndarray
    state_sig: int
    @classmethod
    def from_data(cls, model: mujoco.MjModel, data: mujoco.MjData, state_sig: int) -> StateEvent | None: ...
    def __eq__(self, other: object) -> bool: ...

@dataclasses.dataclass(frozen=True)
class ModelEvent(Event):
    model: mujoco.MjModel
    path: str = ...

@dataclasses.dataclass(frozen=True)
class LoadModelEvent(Event):
    path: str = ...

@dataclasses.dataclass(frozen=True)
class PreloadModelEvent(Event):
    model: mujoco.MjModel

@dataclasses.dataclass(frozen=True)
class PostModelEvent(Event):
    model: mujoco.MjModel
    data: mujoco.MjData
    path: str = ...

@dataclasses.dataclass(frozen=True)
class SingleStepEvent(Event): ...

@dataclasses.dataclass(frozen=True)
class RequestPauseEvent(Event):
    pause_state: sim.PauseState

@dataclasses.dataclass(frozen=True)
class ResetEvent(Event):
    key: int | None = ...

@dataclasses.dataclass(frozen=True, eq=False)
class KeyframeEvent(Event):
    key: int
    state: np.ndarray
    @classmethod
    def from_model(cls, model: mujoco.MjModel, key: int) -> KeyframeEvent | None: ...
    def __eq__(self, other: object) -> bool: ...

@dataclasses.dataclass(frozen=True)
class ThreadPoolEvent(Event):
    nthread: int

@dataclasses.dataclass(frozen=True)
class PreStepEvent(Event):
    model: mujoco.MjModel
    data: mujoco.MjData

@dataclasses.dataclass(frozen=True)
class StepEvent(Event):
    model: mujoco.MjModel
    data: mujoco.MjData

@dataclasses.dataclass(frozen=True)
class PostStepEvent(Event):
    model: mujoco.MjModel
    data: mujoco.MjData

@dataclasses.dataclass(frozen=True)
class UpdateEvent(Event): ...
@dataclasses.dataclass(frozen=True)
class BuildGuiEvent(Event): ...

@dataclasses.dataclass(frozen=True)
class MjOptionSnapshot(Snapshot):
    opt: mujoco.MjOption

@dataclasses.dataclass(frozen=True)
class StepControlSnapshot(Snapshot):
    pause_state: sim.PauseState = ...
    speed: float = ...
    noise_scale: float = ...
    noise_rate: float = ...
    speed_measured: float = ...
    @classmethod
    def from_step_control(cls, step_control: sim.StepControl, speed_measured: float = -1.0) -> StepControlSnapshot: ...

@dataclasses.dataclass(frozen=True)
class ExitEvent(Event):
    reason: str = ...

def describe_exception(ex: BaseException | None) -> str: ...

@dataclasses.dataclass(frozen=True)
class HotReloadEvent(Event):
    plugins: tuple[Any, ...]

@dataclasses.dataclass(frozen=True)
class _HandlerInfo:
    priority: int
    message_type: type[Message]

class Priority(enum.IntEnum):
    INTERNAL = 1
    LIBRARY = 10
    USER = 100
    CRITICAL = 1000

def handler(fn: Callable[..., Any] | None = None, *, priority: int = ...) -> Callable[..., Any]: ...
