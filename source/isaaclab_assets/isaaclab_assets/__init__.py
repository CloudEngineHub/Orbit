# Copyright (c) 2022-2026, The Isaac Lab Project Developers (https://github.com/isaac-sim/IsaacLab/blob/main/CONTRIBUTORS.md).
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause
"""Package containing asset and sensor configurations."""

import os
import toml

# Conveniences to other module directories via relative paths
ISAACLAB_ASSETS_EXT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../"))
"""Path to the extension source directory."""

ISAACLAB_ASSETS_DATA_DIR = os.path.join(ISAACLAB_ASSETS_EXT_DIR, "data")
"""Path to the extension data directory."""

ISAACLAB_ASSETS_METADATA = toml.load(os.path.join(ISAACLAB_ASSETS_EXT_DIR, "config", "extension.toml"))
"""Extension metadata dictionary parsed from the extension.toml file."""

# Configure the module-level variables
__version__ = ISAACLAB_ASSETS_METADATA["package"]["version"]


# --
# Lazy import the robots and sensors
# --

from typing import TYPE_CHECKING
from lazy_imports import LazyModule as _LazyModule, as_package

_mod = _LazyModule(
    *as_package(__file__),
    "from .robots import *",
    "from .sensors import *",
    name=__name__,
)

if TYPE_CHECKING:
    from .robots import *
    from .sensors import *
else:
    __getattr__ = _mod.__getattr__
    __dir__ = _mod.__dir__
    __all__ = _mod.__all__
