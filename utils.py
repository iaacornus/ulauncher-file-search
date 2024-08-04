from os import environ
def check_desktop_env() -> str:
    """
    Check the current desktop environment.

    Returns:
        desktop: str - the desktop environment variable.
    """

    desktop: str = environ.get("DESKTOP_SESSION") or ""
    return desktop.lower()

