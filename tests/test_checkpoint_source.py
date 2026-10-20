"""Tests for checkpoint sources."""

from pathlib import Path
from types import SimpleNamespace

import pytest
import wandb

from mjlab.utils.checkpoint_source import (
  CheckpointInfo,
  CheckpointSource,
  LocalCheckpointSource,
  WandbCheckpointSource,
  make_checkpoint_source,
)
from mjlab.utils.os import get_checkpoint_path


class _StaticCheckpointSource(CheckpointSource):
  """Custom source resolved by import path in the tests below."""

  label = "Static"

  def list_checkpoints(self) -> list[CheckpointInfo]:
    return [CheckpointInfo("model_5.pt", 0.0)]

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


def test_make_checkpoint_source_from_alias_and_import_path(run_dir):
  local = make_checkpoint_source("local", str(run_dir), run_dir.parent)
  assert isinstance(local, LocalCheckpointSource)

  custom = make_checkpoint_source(
    f"{__name__}:_StaticCheckpointSource", "run-id", run_dir.parent
  )
  assert isinstance(custom, _StaticCheckpointSource)
  assert custom.resolve() == (run_dir.parent / "model_5.pt", False)


@pytest.mark.parametrize(
  ("source", "error"),
  [("mlflow", ValueError), ("pathlib:Path", TypeError)],
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


def test_local_resume_skips_checkpoint_caches(run_dir):
  cache = run_dir.parent / "zzz_checkpoints" / "run"
  cache.mkdir(parents=True)
  (cache / "model_1.pt").touch()
  assert get_checkpoint_path(run_dir.parent) == run_dir / "model_100.pt"
