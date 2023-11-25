from minesweeper import Board





game = Board(10)
game.add_mines(15)
game.debug_print_board()
print('mines', game.debug_count_mines())
