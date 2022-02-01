"""Host custom exceptions."""


class DesktopAutomatorError(Exception):
    """Base exception."""


class UnsopportedSystemError(DesktopAutomatorError):
    """Unsupported system error."""
