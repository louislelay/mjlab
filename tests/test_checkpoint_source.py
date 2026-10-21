"""Tests for checkpoint sources."""

from pathlib import Path
from types import SimpleNamespace

import pytest
import wandb

from mjlab.scripts.play import _make_checkpoint_manager
from mjlab.utils.checkpoint_source import (
  CheckpointInfo,
  CheckpointSource,
  LocalCheckpointSource,
  WandbCheckpointSource,
  make_checkpoint_source,
)
from mjlab.viewer.base import PolicyProtocol


class _StaticCheckpointSource(CheckpointSource):
  """Custom source resolved by import path in the tests below."""

  label = "Static"

  def list_checkpoints(self) -> list[CheckpointInfo]:
    return [CheckpointInfo("model_10.pt", 0.0), CheckpointInfo("model_5.pt", 0.0)]

  def download(self, name: str) -> tuple[Path, bool]:
    return self.cache_root / name, False


@pytest.fixture
def run_dir(tmp_path: Path) -> Path:
  run_dir = tmp_path / "2025-01-01_00-00-00"
  run_dir.mkdir()
  for name in ("model_50.pt", "model_100.pt", "model_9.pt", "other.pt"):
    (run_dir / name).touch()
  return run_dir


def test_local_source_resolves_latest_and_named(run_dir):
  source = LocalCheckpointSource(str(run_dir), run_dir.parent)
  assert source.resolve() == (run_dir / "model_100.pt", True)
  assert source.resolve("model_9.pt") == (run_dir / "model_9.pt", True)
  with pytest.raises(ValueError, match="not found"):
    source.resolve("model_7.pt")


def test_make_checkpoint_source_from_import_path(tmp_path):
  source = make_checkpoint_source(
    f"{__name__}:_StaticCheckpointSource", "run-id", tmp_path
  )
  assert isinstance(source, _StaticCheckpointSource)
  assert source.resolve() == (tmp_path / "model_10.pt", False)


@pytest.mark.parametrize(
  ("source", "error"),
  [("local", ValueError), ("pathlib:Path", TypeError)],
)
def test_make_checkpoint_source_rejects_invalid(source, error, tmp_path):
  with pytest.raises(error):
    make_checkpoint_source(source, "run-id", tmp_path)


def test_wandb_source_downloads_latest_into_cache(monkeypatch, tmp_path):
  downloaded: list[tuple[str, str]] = []

  def make_file(name: str) -> SimpleNamespace:
    def download(root: str, replace: bool) -> None:
      downloaded.append((name, root))
      (Path(root) / name).touch()

    return SimpleNamespace(
      name=name, updated_at="2025-01-01T00:00:00Z", download=download
    )

  files = {n: make_file(n) for n in ("model_100.pt", "model_2000.pt", "agent.pt")}
  run = SimpleNamespace(
    load=lambda: None,
    files=lambda pattern: list(files.values()),
    file=lambda name: files[name],
  )
  monkeypatch.setattr(wandb, "Api", lambda: SimpleNamespace(run=lambda path: run))

  source = WandbCheckpointSource("entity/project/abc123", tmp_path)
  cache_dir = tmp_path / "wandb_checkpoints" / "abc123"

  assert source.resolve() == (cache_dir / "model_2000.pt", False)
  assert source.resolve() == (cache_dir / "model_2000.pt", True)
  assert downloaded == [("model_2000.pt", str(cache_dir))]


def test_checkpoint_manager_lists_by_step_and_loads_downloads(tmp_path):
  loaded: list[str] = []

  def load_policy(path: str) -> PolicyProtocol:
    loaded.append(path)
    return lambda obs: obs

  source = _StaticCheckpointSource("run-id", tmp_path)
  manager = _make_checkpoint_manager(source, "model_10.pt", load_policy)

  assert [name for name, _ in manager.fetch_available()] == [
    "model_5.pt",
    "model_10.pt",
  ]
  manager.load_checkpoint("model_5.pt")
  assert loaded == [str(tmp_path / "model_5.pt")]
  assert manager.source_label == "Static"
