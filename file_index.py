from os import system, environ
from os.path import exists, isfile


def explore_dir(DIR: str):

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

    system( # batshit subprocess.call doesnt work for some reason
        " ".join(cmd)
    )


def find_dir(HOME: str) -> list[str]:
    """
    Find all the DIR in $HOME.

    Parameters:
        HOME: str - $HOME

    Returns:
        DIRS: list[str] - list of all dir in $HOME.
    """

    DIRS: list[str] = []
    explore_dir(HOME)

    if not isfile("dirs_home.txt"):
        raise SystemExit()

    with open("dirs_home.txt", "r", encoding="utf-8") as dirs_:
        for dir_ in dirs_:
            if exists(_dir_ := dir_.strip("\n")):
                DIRS.append(_dir_)

    return DIRS


def index_files(DIRS: list[str]):

    print(DIRS)
    for dir_ in DIRS:
        _dir_: str = dir_.split("/")[-1]
        if _dir_.startswith("."):
            continue

        explore_dir(dir_)

