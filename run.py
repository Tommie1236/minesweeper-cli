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
    DIFFICULTY = 'd'


def main(stdscr):
    
    window = Window.MENU

    curses.curs_set(0)
    curses.cbreak()
    
    active = True

    l, c = curses.LINES, curses.COLS
    center = (l//2, c//2)
    big_screen = l > 20 and c > 80
    
    stdscr.keypad(True)

    # menu indexes
    menu_selected = 0
    set_selected = 0

    while active:
        stdscr.clear()
        match window:
            case Window.MENU:
                if big_screen:
                    i = 0
                    for line in open('assets/minelogo.txt', 'r').readlines():
                        stdscr.addstr((l // 5) + i, center[1] - len(line) // 2, line)
                        i += 1
                else:
                    stdscr.addstr(3, center[1] - 6, 'MINESWEEPER')
                
                i = 0
                for line in open('assets/controls-menu.txt', 'r'):
                    stdscr.addstr(l - 8 + i, c - 18, line)
                    i += 1

                stdscr.refresh()

                while True:
                    
                    stdscr.addstr(center[0] -2 if big_screen else 5, center[1] - 4, '1. Play',     curses.A_REVERSE if menu_selected == 0 else curses.A_NORMAL)
                    stdscr.addstr(center[0] -1 if big_screen else 6, center[1] - 4, '2. Settings', curses.A_REVERSE if menu_selected == 1 else curses.A_NORMAL)
                    stdscr.addstr(center[0]    if big_screen else 7, center[1] - 4, '3. Quit',     curses.A_REVERSE if menu_selected == 2 else curses.A_NORMAL)
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
                            menu_selected = (menu_selected + 1) % 3
                        case 259: # up
                            menu_selected = (menu_selected - 1) % 3
                        case 10 | 261: # enter
                            match menu_selected:
                                case 0: # play
                                    window = Window.GAME
                                    break
                                case 1: # settings
                                    window = Window.SETTINGS
                                    break
                                case 2: # quit
                                    active = False
                                    break   
                        case 260: # left
                            active = False
                            break
                        

            case Window.SETTINGS:
                stdscr.clear()
                stdscr.addstr(0, 0, 'SETTINGS')
                if big_screen:
                    i = 0
                    for line in open('minelogo.txt', 'r').readlines():
                        stdscr.addstr((l // 5) + i, center[1] - len(line) // 2, line)
                        i += 1
                else:
                    stdscr.addstr(3, center[1] - 6, 'MINESWEEPER')
                stdscr.refresh()

                
                while True:
                    
                    stdscr.addstr(center[0] -2 if big_screen else 5, center[1] - 4, '1. Difficulty', curses.A_REVERSE if set_selected == 0 else curses.A_NORMAL)
                    stdscr.addstr(center[0] -1 if big_screen else 6, center[1] - 4, '2. Colors', curses.A_REVERSE if set_selected == 1 else curses.A_NORMAL)
                    stdscr.addstr(center[0] if big_screen else 7, center[1] - 4, '3. Back', curses.A_REVERSE if set_selected == 2 else curses.A_NORMAL)
                    stdscr.refresh()

                    key = stdscr.getch()
                    match key:
                        case 49: # 1 (difficulty)
                            window = Window.DIFFICULTY
                            break
                        case 50: # 2 (colors)
                            stdscr.addstr(0, 0, 'COLORS (not implemented yet)')
                            stdscr.refresh()
                            pass
                        case 51: # 3 (back)
                            window = Window.MENU
                            break
                        case 258: # down
                            set_selected = (set_selected + 1) % 3
                        case 259: # up
                            set_selected = (set_selected - 1) % 3
                        case 10 | 261: # enter
                            match set_selected:
                                case 0: # difficulty
                                    window = Window.DIFFICULTY
                                    break
                                case 1: # colors
                                    stdscr.addstr(0, 0, 'COLORS (not implemented yet)')
                                    stdscr.refresh()
                                    pass
                                case 2: # back
                                    window = Window.MENU
                                    break
                        case 260: # left
                            window = Window.MENU
                            break


            case Window.GAME:
                stdscr.clear()
                stdscr.addstr(0, 0, 'GAME')
                stdscr.refresh()
                pass
            case Window.DIFFICULTY:
                stdscr.clear()
                stdscr.addstr(0, 0, 'DIFFICULTY')
                stdscr.refresh()
                pass




if __name__ == '__main__':
    mystdout = StdOutWrapper()
    sys.stdout = mystdout
    sys.stderr = mystdout
    wrapper(main)

    sys.stdout = sys.__stdout__
    sys.stderr = sys.__stderr__
    sys.stdout.write(mystdout.get_text())