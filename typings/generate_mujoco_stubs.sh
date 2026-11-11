#!/usr/bin/env bash

# Generate type stubs for MuJoCo using pybind11-stubgen.
# This helps suppress pyright/ty errors for MuJoCo's C++ bindings.
#
# The output is post-processed by postprocess_stubs.py to make it
# platform-independent (it drops the OpenGL backend stubs, which differ between
# macOS and Linux). This keeps the committed stubs identical on every platform,
# so CI can regenerate them and fail if they drift from the installed mujoco
# version. pybind11-stubgen is pinned so its output is reproducible.

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# --no-sync runs in the already-synced project environment (so mujoco is
# importable) without disturbing it; the conflicting cpu/cu130 extras mean a
# plain "uv run" would re-sync and churn the environment.
STUBGEN_VERSION="2.5.5"
STUBGEN=(uv run --no-sync --with "pybind11-stubgen==${STUBGEN_VERSION}" pybind11-stubgen)

echo "Generating MuJoCo type stubs..."
"${STUBGEN[@]}" mujoco -o "$SCRIPT_DIR" --ignore-all-errors

# The MuJoCo Studio modules used by the native viewer, and the Filament
# renderer (shipped with Studio) used by the offscreen renderer. Studio loads its
# windowing and rendering libraries on import, which may fail on a headless
# machine; skip it in that case rather than failing, keeping the committed stubs.
#
# Compiled extension modules are stubbed with pybind11-stubgen. The pure-Python
# modules are stubbed from source with mypy's stubgen, which (unlike
# pybind11-stubgen) records instance attributes assigned in __init__.
STUDIO_EXTENSION_MODULES=(
  mujoco._render_filament
  mujoco.studio.dear_imgui.dear_imgui
  mujoco.studio.implot.implot
  mujoco.studio.ux
)
STUDIO_PYTHON_MODULES=(
  mujoco.mjrf
  mujoco.rendering
  mujoco.rendering.filament
  mujoco.rendering.filament.renderer
  mujoco.studio
  mujoco.studio.app
  mujoco.studio.app.inputs
  mujoco.studio.app.plugins
  mujoco.studio.launch_passive
  mujoco.studio.messages
  mujoco.studio.plugin
  mujoco.studio.viewer_handle
  mujoco.studio.viewer_protocol
)
MYPY_VERSION="1.18.2"
MYPY_STUBGEN=(uv run --no-sync --with "mypy==${MYPY_VERSION}" stubgen)

if uv run --no-sync python -c "import mujoco.studio.ux"; then
  for module in "${STUDIO_EXTENSION_MODULES[@]}"; do
    "${STUBGEN[@]}" "$module" -o "$SCRIPT_DIR" --ignore-all-errors
  done
  "${MYPY_STUBGEN[@]}" "${STUDIO_PYTHON_MODULES[@]/#/-m}" -o "$SCRIPT_DIR"
else
  echo "Warning: could not import mujoco.studio. Skipping its stubs."
fi

echo "Post-processing stubs to make them platform-independent..."
uv run --no-sync python "$SCRIPT_DIR/postprocess_stubs.py"

echo "MuJoCo stubs generated successfully in $SCRIPT_DIR/mujoco/"
