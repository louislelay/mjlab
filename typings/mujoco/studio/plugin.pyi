import os
from _typeshed import Incomplete
from collections.abc import Iterable
from mujoco.studio import messages as messages, viewer_handle as viewer_handle, viewer_protocol as viewer_protocol

SimInitEvent: Incomplete
ViewerInitEvent: Incomplete
ThemeEvent: Incomplete

class SimPlugin:
    @property
    def handle(self) -> viewer_handle.ViewerHandle: ...
    @handle.setter
    def handle(self, value: viewer_handle.ViewerHandle | None) -> None: ...

class ViewerPlugin:
    @property
    def viewer(self) -> viewer_protocol.Viewer: ...
    @viewer.setter
    def viewer(self, value: viewer_protocol.Viewer | None) -> None: ...
Plugin = SimPlugin | ViewerPlugin

def split_plugins(plugins: Iterable[Plugin] | None = None) -> tuple[list[ViewerPlugin], list[SimPlugin]]: ...

PLUGIN_PACKAGE: str

def load_plugins(paths: Iterable[str | os.PathLike[str]] | None = None) -> list[Plugin]: ...
