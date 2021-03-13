
import curses

from config import moods
from interface import graphical_interface


def main():
    
    curses.wrapper(graphical_interface, moods)

main()
