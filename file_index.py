from os import system, environ
from os.path import exists, isfile


def explore_dir(DIR: str) -> None:
    """
    Explores the provided dir.

    Parameters:
        DIR: str - directory to be explored.

    Returns:
        None.
    """

    # set maxdepth=1 if the dir is $HOME.
    if DIR == f"{environ.get('HOME')}":
        cmd: list[str] = [
                "find",
                f"{DIR}",
                "-maxdepth", "1",
                "-type", "d",
                "-name", "'*'",
                ">",
                "dirs_home.txt"
            ]
    else:
        cmd: list[str] = [
                "find",
                f"{DIR}",
                "-type", "f",
                "-name", "'*'",
                ">",
                "dirs.txt"
            ]

    # batshit subprocess.call
    # doesnt work for some reason
    system(
        " ".join(cmd)
    )


def list_dirs(HOME: str) -> list[str]:
    """
    Find all the DIR in $HOME.

    Parameters:
        HOME: str - $HOME

    Returns:
        DIRS: list[str] - list of all dir in $HOME.
    """

    DIRS: list[str] = []
    if not isfile("dirs_home.txt"):
        explore_dir(HOME)

    with open(
            "dirs_home.txt", "r", encoding="utf-8"
        ) as dirs_:
        for dir_ in dirs_:
            if exists(_dir_ := dir_.strip("\n")):
                DIRS.append(_dir_)

    return DIRS


def index_files(DIRS: list[str], HOME: str) -> None:
    """
    Index all files in given array of dir.

    Parameters:
        DIRS: list[str] - array of dir.
        HOME: str - $HOME.

    Returns:
        None.
    """

    if not DIRS:
        raise SystemExit("Cannot index files.")

    for dir_ in DIRS:
        _dir_: str = dir_.replace(f"{HOME}/", "")
        if _dir_.startswith(".") or _dir_ == HOME:
            continue

        explore_dir(dir_)
