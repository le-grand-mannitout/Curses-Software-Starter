
import curses
import os
from typing import Union

from config import moods
from interface import graphical_interface


def are_mood(moods: dict) -> Union[type, bool]:
    """Raise if dict is empty."""
    if not moods:
        raise IndexError("There is no mood in config file")

    else:
        return True


def execute_task(softwares_to_launch: tuple):
    """Execute software tuple."""
    for software in softwares_to_launch:
        os.system(f"{software} &")


def main():

    if are_mood(moods):
        softwares_to_launch = curses.wrapper(graphical_interface, moods)
        execute_task(softwares_to_launch)


main()
