from os import environ
from os.path import exists


def check_desktop_env() -> str:
    """
    Check the current desktop environment.

    Returns:
        desktop: str - the desktop environment variable.
    """

    desktop: str = environ.get("DESKTOP_SESSION") or ""
    return desktop.lower()

def find_icons(HOME: str, icon_theme: str) -> list[str]:
    """
    Find the icons currently used by the system.

    Parameters:
        HOME: str - path of user home dir.
        icon_theme: str - currently set icon theme.

    Returns:
        existing_dir: list[str] - the path of currently set icon theme.
    """

    ICON_DIR: list[str] = [
            "/usr/share/icons",
            f"{HOME}/.local/share/icons"
            f"{HOME}/.icons",
        ]
    existing_dir: list[str] = []

    for dir_ in ICON_DIR:
        if exists(icon_theme_dir_ := f"{dir_}/{icon_theme}"):
            existing_dir.append(icon_theme_dir_)

    return existing_dir
