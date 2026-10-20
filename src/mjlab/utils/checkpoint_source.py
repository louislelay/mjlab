"""Sources that list and fetch the checkpoints of a training run."""

from __future__ import annotations

import importlib
import re
from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any

_STEP_PATTERN = re.compile(r"^model_(\d+)\.pt$")


@dataclass(frozen=True)
class CheckpointInfo:
  """A checkpoint available from a source."""

  name: str
  """File name, e.g. ``model_4000.pt``."""
  updated_at: float
  """Last modification time as a POSIX timestamp."""

  @property
  def step(self) -> int:
    """Training iteration parsed from ``model_<step>.pt``, or 0 if absent."""
    match = _STEP_PATTERN.match(self.name)
    return int(match.group(1)) if match else 0


class CheckpointSource(ABC):
  """Lists and fetches the checkpoints of a single training run.

  Sources are built as ``cls(run, cache_root)``. ``run`` identifies the run in the
  backend, and ``cache_root`` is the experiment log directory. Remote sources should
  cache downloads in a subdirectory of ``cache_root`` whose name ends with
  ``_checkpoints``, which local resume skips when looking for runs.
  """

  label: str = "Remote"
  """Backend name shown in logs and in the viewer."""

  def __init__(self, run: str, cache_root: Path) -> None:
    self.run = run
    self.cache_root = cache_root

  @abstractmethod
  def list_checkpoints(self) -> list[CheckpointInfo]:
    """List the ``.pt`` checkpoints of the run."""

  @abstractmethod
  def download(self, name: str) -> tuple[Path, bool]:
    """Return a local path to checkpoint ``name``, downloading it if needed.

    Returns:
      The local path and whether it was already cached.
    """

  @property
  def run_name(self) -> str | None:
    """Human-readable run name, if the backend has one."""
    return None

  @property
  def run_url(self) -> str | None:
    """URL of the run in the backend's UI, if any."""
    return None

  @property
  def run_status(self) -> str | None:
    """Status of the run (e.g. ``"running"``), if the backend reports one."""
    return None

  def resolve(self, name: str | None = None) -> tuple[Path, bool]:
    """Fetch checkpoint ``name``, or the latest ``model_<step>.pt`` if None.

    Returns:
      The local path and whether it was already cached.
    """
    available = [c for c in self.list_checkpoints() if _STEP_PATTERN.match(c.name)]
    if not available:
      raise ValueError(f"No model_<step>.pt checkpoint found in run {self.run}.")
    names = [c.name for c in available]
    if name is None:
      return self.download(max(available, key=lambda c: c.step).name)
    if name not in names:
      raise ValueError(
        f"Checkpoint '{name}' not found in run {self.run}. Available: {names}"
      )
    return self.download(name)


class LocalCheckpointSource(CheckpointSource):
  """Checkpoints stored in a local run directory, given as ``run``."""

  label = "Local"

  def list_checkpoints(self) -> list[CheckpointInfo]:
    return [
      CheckpointInfo(name=f.name, updated_at=f.stat().st_mtime)
      for f in Path(self.run).glob("*.pt")
    ]

  def download(self, name: str) -> tuple[Path, bool]:
    return Path(self.run) / name, True


class WandbCheckpointSource(CheckpointSource):
  """Checkpoints uploaded to a W&B run, given as ``entity/project/run_id``."""

  label = "W&B"

  def __init__(self, run: str, cache_root: Path) -> None:
    super().__init__(run, cache_root)
    # Imported lazily because importing wandb is slow.
    import wandb

    self.wandb_run: Any = wandb.Api().run(run)
    """The ``wandb.apis.public.Run``, e.g. to look up artifacts it used."""
    self._cache_dir = cache_root / "wandb_checkpoints" / run.split("/")[-1]

  @property
  def run_name(self) -> str:
    return _parse_wandb_dt(self.wandb_run.created_at).strftime("%Y-%m-%d_%H-%M-%S")

  @property
  def run_url(self) -> str:
    return self.wandb_run.url

  @property
  def run_status(self) -> str:
    return self.wandb_run.state

  def list_checkpoints(self) -> list[CheckpointInfo]:
    self.wandb_run.load()
    return [
      CheckpointInfo(name=f.name, updated_at=_parse_wandb_dt(f.updated_at).timestamp())
      for f in self.wandb_run.files(pattern="%.pt")
      if f.name.endswith(".pt")
    ]

  def download(self, name: str) -> tuple[Path, bool]:
    path = self._cache_dir / name
    if path.exists():
      return path, True
    self._cache_dir.mkdir(parents=True, exist_ok=True)
    self.wandb_run.file(name).download(str(self._cache_dir), replace=True)
    return path, False


_BUILTIN_SOURCES: dict[str, type[CheckpointSource]] = {
  "local": LocalCheckpointSource,
  "wandb": WandbCheckpointSource,
}


def make_checkpoint_source(source: str, run: str, cache_root: Path) -> CheckpointSource:
  """Build a checkpoint source from an alias or an import path.

  Args:
    source: ``"local"``, ``"wandb"``, or the import path of a
      :class:`CheckpointSource` subclass (e.g. ``"my_pkg.sources:MySource"``).
    run: Identifier of the run in that backend.
    cache_root: Experiment log directory, under which downloads are cached.

  Returns:
    The constructed source.
  """
  source_cls = _BUILTIN_SOURCES.get(source) or _import_source_class(source)
  return source_cls(run, cache_root)


def _import_source_class(path: str) -> type[CheckpointSource]:
  module_name, sep, attr = path.partition(":")
  if not sep:
    raise ValueError(
      f"Unknown checkpoint source {path!r}. Expected one of "
      f"{sorted(_BUILTIN_SOURCES)} or an import path like 'my_pkg.sources:MySource'."
    )
  source_cls = getattr(importlib.import_module(module_name), attr)
  if not (isinstance(source_cls, type) and issubclass(source_cls, CheckpointSource)):
    raise TypeError(f"{path!r} is not a CheckpointSource subclass.")
  return source_cls


def _parse_wandb_dt(value: str | datetime) -> datetime:
  """Parse a W&B datetime string (or pass through a datetime object)."""
  if isinstance(value, str):
    return datetime.fromisoformat(value.replace("Z", "+00:00"))
  return value
