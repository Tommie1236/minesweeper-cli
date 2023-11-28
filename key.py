import curses

window = curses.initscr()
curses.noecho()
window.keypad(True)  # Maybe not perfect, but a good start?

while True:
    k = window.getch()
    print(f'k: {k}')
    curses.flushinp()