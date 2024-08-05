from os import system
from os.path import exists, isfile


def explore_dir(DIR: str):

    if DIR == f"{HOME}":
        cmd: list[str] = [
                "find",
                f"{DIR}",
                "-maxdepth", "1",
                "-type", "d",
                "-name", "'*'",
                ">>",
                "dirs_home.txt"
            ]
    else:
        cmd: list[str] = [
                "find",
                f"{DIR}"
                "-type", "f",
                "-name", "'*'",
                ">>",
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
    system( # batshit subprocess.call doesnt work for some reason
        " ".join(
            [
                "find",
                f"{HOME}",
                "-maxdepth", "1",
                "-type", "d",
                "-name", "'*'",
                ">>",
                "dirs.txt"
            ]
        )
    )

    if not isfile("dirs.txt"):
        raise SystemExit()

    with open("dirs.txt", "r", encoding="utf-8") as dirs_:
        for dir_ in dirs_:
            if exists(_dir_ := dir_.strip("\n")):
                DIRS.append(_dir_)

    return DIRS

