"""Host constant variables."""

import os
import sys

from desktopautomator.exceptions import UnsopportedSystemError

PLATFORM = sys.platform

if PLATFORM == "linux":
    DEFAULT_CONFIG_DIR = f"{os.path.expanduser('~')}/.config/desktopautomator"
elif PLATFORM == "win32":
    DEFAULT_CONFIG_DIR = "..."
else:
    raise UnsopportedSystemError(f"Platform {sys.platform} is not supported")

PROJECT_PATH = os.path.dirname(os.path.realpath(__file__))
DATA_DIR = f"{PROJECT_PATH}/data"

CONFIG_FILE_PATH = os.environ.get(
    "DESKTOP_AUTOMATOR_CONFIG", f"{DEFAULT_CONFIG_DIR}/configuration.yaml"
)
