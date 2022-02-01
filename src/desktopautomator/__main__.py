"""Main file to run desktop automator."""

from desktopautomator.config import config
from desktopautomator.setup import pre_setup


def main() -> None:
    """Run Desktop Automator."""
    pre_setup()
    print(config)


if __name__ == "__main__":
    main()
