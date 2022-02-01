"""Desktop Automator initial setup logic."""

import shutil
from contextlib import suppress

from desktopautomator.const import DATA_DIR, DEFAULT_CONFIG_DIR


def pre_setup() -> None:
    """Do initial setup if needed."""
    with suppress(FileExistsError):
        shutil.copytree(f"{DATA_DIR}/initial_config/", DEFAULT_CONFIG_DIR)
        print(f"Initial config files created at: {DEFAULT_CONFIG_DIR}")
