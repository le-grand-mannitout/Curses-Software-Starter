
import curses


KEY_K = 106
KEY_J = 107
KEY_ENTER = 10

def display_moods(stdscr, mood_names: list):
    """Display moods names on the curses window."""
    stdscr.addstr(0, 0, "--Mood selector--")
    for i, mood in enumerate(mood_names):
        stdscr.addstr(i*2 + 2, 0, f"  {mood}")


def cursor_mov(stdscr,
               mood_names: list,
               index_to_cursor: int):
    """Move the cursor by changing text background color."""
    stdscr.addstr(index_to_cursor,
                  0,
                  "* ")

    stdscr.addstr(index_to_cursor,
                  2,
                  mood_names[(index_to_cursor - 2)//2],
                  curses.color_pair(2))


def graphical_interface(stdscr,
                        mood_dict: dict) -> tuple:
    """Main graphical interface menu."""
    stdscr.clear()
    curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_YELLOW)
    stdscr.attron(curses.color_pair(1))
    curses.curs_set(0)

    mood_names = [mood for mood in mood_dict]

    display_moods(stdscr, mood_names)

    k, cursor = 0, 2
    height, width = stdscr.getmaxyx()

    while 1:

        if k in (curses.KEY_DOWN, KEY_K):
            cursor += 2

        elif k in (curses.KEY_UP, KEY_J):
            cursor -= 2

        elif k == KEY_ENTER:
            return mood_dict[mood_names[(cursor - 2)//2]]

        cursor = max(2, cursor)
        cursor = min(len(mood_names)*2, cursor)

        display_moods(stdscr, mood_names)
        cursor_mov(stdscr, mood_names, cursor)

        stdscr.refresh()
        k = stdscr.getch()
