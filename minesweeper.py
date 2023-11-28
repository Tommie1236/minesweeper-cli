import random

from termcolor import colored



COLORS = {
    0: 'grey',
    1: 'blue',
    2: 'cyan',
    3: 'green',
    4: 'yellow',
    5: 'magenta',
    6: 'red', # termcolor doesn't support more colors so 6+ is red.
    7: 'red',
    8: 'red'
}
class Square_State:
    MARKED = 'M'
    REVEALED = 'R'
    HIDDEN = 'H'

class Square:
# minesweeper board square

    def __init__(self, x:int, y:int):
        self._x = x
        self._y = y
        self._is_mine = False
        self._mines_around = 0
        self._is_marked = False
        self._is_revealed = False

    def __repr__(self) -> str:
        return "X" if self._is_mine else colored(str(self._mines_around), COLORS[self._mines_around])

    def __str__(self) -> str:
        return "X" if self._is_mine else colored(str(self._mines_around), COLORS[self._mines_around])

    def set_mine(self) -> bool:
        self._is_mine = True
        return self._is_mine

    def is_mine(self) -> bool:
        return self._is_mine
    
    def add_mine(self) -> int:
        self._mines_around += 1
        return self._mines_around

    def get_mines_around(self) -> int:
        return self._mines_around
    
    def get_coords(self) -> tuple[int, int]:
        return self._x, self._y
    
    def mark(self) -> bool:
        self._is_marked = True
        return self._is_marked

    def reveal(self) -> bool:
        self._is_revealed = True
        return self._is_revealed

    def is_revealed(self) -> tuple[bool, int]:
        return self._is_revealed, self._mines_around
    
    def is_marked(self) -> bool:
        return self._is_marked
    
    def get_state(self):

        if self._is_revealed:
            return Square_State.REVEALED
        elif self._is_marked:
            return Square_State.MARKED
        else:
            return Square_State.HIDDEN

    def dig(self) -> tuple[bool, int]:
        # dig the square
        self._is_revealed = True
        return self._is_mine, self._mines_around


class Board:
# minesweeper board


    def __init__(self, size:int) -> None:
        self._size = size
        self._generate_board()

    def _generate_board(self) -> bool:
        # generate the board of specified size
        self._board = [ [Square(i, j) for i in range(self._size)] for j in range(self._size)]
        # self.debug_print_board()
        return True

    def add_mines(self, mines:int):
        # add the specified amount of mines to the board
        for i in range(mines):
            x, y = random.randint(0, self._size - 1), random.randint(0, self._size - 1)
            while self._board[x][y].is_mine():
                x, y = random.randint(0, self._size - 1), random.randint(0, self._size - 1)

            self._board[x][y].set_mine()
            neighbors = self.get_neighbors(self._board[x][y])
            for neighbor in neighbors:
                neighbor.add_mine()


    # write a function that retuns all the neighboring squares of a square
    def get_neighbors(self, square: Square) -> list:
        neighbors = []
        x, y = square.get_coords()
        # print('root', x, y)
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (i == 0 and j == 0) or x + i < 0 or x + i >= self._size or y + j < 0 or y + j >= self._size:
                    # print('continue', x + i, y + j)
                    continue
                # print('append', x + i, y + j)
                neighbors.append(self._board[y + j][x + i])
        # print('neighbors', [neighbor.get_coords() for neighbor in neighbors])
        return neighbors


    # debug functions
    def debug_print_board(self, show_coords:bool = False):
        # print the board
        print('MINESWEEPER BOARD')
        if show_coords: print('  0 1 2 3 4 5 6 7 8 9')
        for row in self._board:
            if show_coords: print(row[0]._y, end=' ')
            for col in row:
                print(col, end=' ')
            print('')


    def debug_count_mines(self) -> int:
        mines = 0
        for row in self._board:
            for col in row:
                if col.is_mine():
                    mines += 1

        return mines





    