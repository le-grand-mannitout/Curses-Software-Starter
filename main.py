
import curses
import os

from config import moods
from interface import graphical_interface


def execute_task(softwares_to_launch: tuple):
    """
        Execute software tuple
    """
    for software in softwares_to_launch:
        os.system(f"{software} &")


def main():

    softwares_to_launch = curses.wrapper(graphical_interface, moods)
    execute_task(softwares_to_launch)


main()
