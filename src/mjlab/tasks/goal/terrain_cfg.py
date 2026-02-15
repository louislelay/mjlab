"""Terrain configurations for goal-reaching tasks.

Provides terrain distributions inspired by AME-2's training curriculum:
  - Dense (~25%): rough heightfields, random grids, discrete obstacles
  - Climbing (~30%): pyramid stairs (up/down), open stairs, random stairs
  - Sparse (~45%): stepping stones, narrow beams, nested rings

All sub-terrains have FlatPatchSamplingCfg("goal_targets") enabled so the
goal command can sample walkable goal positions.
"""

import mjlab.terrains as terrain_gen
from mjlab.terrains.terrain_generator import (
  FlatPatchSamplingCfg,
  TerrainGeneratorCfg,
)

# Shared flat patch config applied to every sub-terrain.
_GOAL_PATCH_CFG = {
  "goal_targets": FlatPatchSamplingCfg(
    num_patches=20,
    patch_radius=0.4,
    max_height_diff=0.05,
  )
}


GOAL_REACHING_TERRAINS_CFG = TerrainGeneratorCfg(
  size=(8.0, 8.0),
  border_width=20.0,
  num_rows=15,
  num_cols=30,
  curriculum=True,
  sub_terrains={
    # ---- Dense (~25%) ----
    "random_rough": terrain_gen.HfRandomUniformTerrainCfg(
      proportion=0.10,
      noise_range=(0.02, 0.15),
      noise_step=0.02,
      border_width=0.25,
      flat_patch_sampling=_GOAL_PATCH_CFG,
    ),
    "random_grid": terrain_gen.BoxRandomGridTerrainCfg(
      proportion=0.08,
      grid_width=0.4,
      grid_height_range=(0.0, 0.35),
      platform_width=1.0,
      flat_patch_sampling=_GOAL_PATCH_CFG,
    ),
    "discrete_obstacles": terrain_gen.HfDiscreteObstaclesTerrainCfg(
      proportion=0.07,
      obstacle_width_range=(0.3, 1.0),
      obstacle_height_range=(0.05, 0.35),
      num_obstacles=50,
      border_width=0.25,
      flat_patch_sampling=_GOAL_PATCH_CFG,
    ),
    # ---- Climbing (~30%) ----
    "pyramid_stairs_up": terrain_gen.BoxPyramidStairsTerrainCfg(
      proportion=0.08,
      step_height_range=(0.05, 0.20),
      step_width=0.3,
      platform_width=2.0,
      border_width=1.0,
      flat_patch_sampling=_GOAL_PATCH_CFG,
    ),
    "pyramid_stairs_down": terrain_gen.BoxInvertedPyramidStairsTerrainCfg(
      proportion=0.08,
      step_height_range=(0.05, 0.20),
      step_width=0.3,
      platform_width=2.0,
      border_width=1.0,
      flat_patch_sampling=_GOAL_PATCH_CFG,
    ),
    "open_stairs": terrain_gen.BoxOpenStairsTerrainCfg(
      proportion=0.07,
      step_height_range=(0.08, 0.22),
      step_width_range=(0.35, 0.8),
      platform_width=1.0,
      border_width=0.25,
      flat_patch_sampling=_GOAL_PATCH_CFG,
    ),
    "random_stairs": terrain_gen.BoxRandomStairsTerrainCfg(
      proportion=0.07,
      step_width=0.7,
      step_height_range=(0.08, 0.30),
      platform_width=1.0,
      border_width=0.25,
      flat_patch_sampling=_GOAL_PATCH_CFG,
    ),
    # ---- Sparse (~45%) ----
    "stepping_stones": terrain_gen.BoxSteppingStonesTerrainCfg(
      proportion=0.18,
      stone_size_range=(0.35, 0.8),
      stone_distance_range=(0.1, 0.8),
      stone_height=0.2,
      stone_height_variation=0.15,
      stone_size_variation=0.15,
      displacement_range=0.15,
      floor_depth=2.0,
      platform_width=1.0,
      border_width=0.25,
      flat_patch_sampling=_GOAL_PATCH_CFG,
    ),
    "narrow_beams": terrain_gen.BoxNarrowBeamsTerrainCfg(
      proportion=0.14,
      num_beams=14,
      beam_width_range=(0.15, 0.6),
      beam_height=0.2,
      spacing=0.8,
      platform_width=1.0,
      border_width=0.25,
      floor_depth=2.0,
      flat_patch_sampling=_GOAL_PATCH_CFG,
    ),
    "nested_rings": terrain_gen.BoxNestedRingsTerrainCfg(
      proportion=0.13,
      num_rings=8,
      ring_width_range=(0.25, 0.6),
      gap_range=(0.1, 0.45),
      height_range=(0.1, 0.4),
      platform_width=1.0,
      border_width=0.25,
      floor_depth=2.0,
      flat_patch_sampling=_GOAL_PATCH_CFG,
    ),
  },
  add_lights=True,
)