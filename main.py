
import curses
import os

from config import moods
from interface import graphical_interface


def execute_task(softwares_to_launch):
    
    if isinstance(softwares_to_launch, tuple):
        for software in softwares_to_launch:
            os.system(f"{software} &")
            
    else: os.system(f"{softwares_to_launch} &")

def main():
    
    softwares_to_launch = curses.wrapper(graphical_interface, moods)
    execute_task(softwares_to_launch)

main()
