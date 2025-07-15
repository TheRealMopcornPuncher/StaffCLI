import curses
import pyaudio
from curses import wrapper

def main(stdscr):
    stdscr.clear()
    stdscr.addstr(10, 20, "Why is it called 'addstr' and not just print like literally everyone and everything else, I hate this")
    stdscr.refresh()
    stdscr.getch()

wrapper(main)