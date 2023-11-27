from minesweeper import Board
from curses import wrapper
import curses
import time
import sys


class StdOutWrapper:
    text = ""
    def write(self,txt):
        self.text += txt
        self.text = '\n'.join(self.text.split('\n')[-30:])
    def get_text(self):
        return '\n'.join(self.text.split('\n'))

class Window:
    MENU = 'm'
    GAME = 'g'
    SETTINGS = 's'


def main(stdscr):
    
    window = Window.MENU

    curses.curs_set(0)
    curses.cbreak()
    
    active = True

    l, c = curses.LINES, curses.COLS
    center = (l//2, c//2)
    big_screen = l > 20 and c > 80
    
    stdscr.keypad(True)

    while active:
        stdscr.clear()

        match window:
            case Window.MENU:
                if big_screen:
                    i = 0
                    for line in open('minelogo.txt', 'r').readlines():
                        stdscr.addstr((l // 5) + i, center[1] - len(line) // 2, line)
                        i += 1
                else:
                    stdscr.addstr(3, center[1] - 6, 'MINESWEEPER')
                stdscr.refresh()
                
                selected = 0
                while True:
                    
                    stdscr.addstr(center[0] -2 if big_screen else 5, center[1] - 4, '1. Play', curses.A_REVERSE if selected == 0 else curses.A_NORMAL)
                    stdscr.addstr(center[0] -1 if big_screen else 6, center[1] - 4, '2. Settings', curses.A_REVERSE if selected == 1 else curses.A_NORMAL)
                    stdscr.addstr(center[0] if big_screen else 7, center[1] - 4, '3. Quit', curses.A_REVERSE if selected == 2 else curses.A_NORMAL)
                    stdscr.refresh()
                    
                    key = stdscr.getch()
                    match key:
                        case 49: # 1 (play)
                            window = Window.GAME
                            break
                        case 50: # 2 (settings)
                            window = Window.SETTINGS
                            break
                        case 51: # 3 (quit)
                            active = False
                            break
                        case 258: # down
                            selected = (selected + 1) % 3
                        case 259: # up
                            selected = (selected - 1) % 3
                        case 10 | 261: # enter
                            match selected:
                                case 0: # play
                                    window = Window.GAME
                                    break
                                case 1: # settings
                                    window = Window.SETTINGS
                                    break
                                case 2: # quit
                                    active = False
                                    break
            case Window.SETTINGS:
                pass
            case Window.GAME:
                pass




if __name__ == '__main__':
    mystdout = StdOutWrapper()
    sys.stdout = mystdout
    sys.stderr = mystdout
    wrapper(main)

    sys.stdout = sys.__stdout__
    sys.stderr = sys.__stderr__
    sys.stdout.write(mystdout.get_text())