
import curses


KEY_K = 106
KEY_J = 107

def display_moods(stdscr, mood_names):
    
    for i, mood in enumerate(mood_names):
        stdscr.addstr(i*2, 2, mood)
    

def graphical_interface(stdscr, mood_dict):
    """
        Main graphical interface menu
    """
    stdscr.clear()
    curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    stdscr.attron(curses.color_pair(1))
    
    mood_names = [mood for mood in mood_dict]
    
    display_moods(stdscr, mood_names)
    
    k, cursor = 0, 0
    height, width = stdscr.getmaxyx()
    
    while 1:
        
        if k in (curses.KEY_DOWN, KEY_K):
            cursor += 2
        
        elif k in (curses.KEY_UP, KEY_J):
            cursor -= 2
            
            
        cursor = max(0, cursor)
        cursor = min((len(mood_names)*2) - 2, cursor)
            
        stdscr.move(cursor, 0)
        
        stdscr.refresh()
        k = stdscr.getch()
