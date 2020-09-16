# file for the command line interface (cli)
from .board import board
from .pieces import pawn, rook, knight, bishop, queen, king

b = board()

# function to initiatethe moving of a piece
def move_piece(type, current, new):
    x, y = ['a', 5], ['a', 3]
    if rook.move(b.board, x, y, False):
        return b.update_board(x, y)
    return False