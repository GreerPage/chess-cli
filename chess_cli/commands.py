# file for the command line interface (cli)
from .board import board
from .pieces import pawn, rook, knight, bishop, queen, king

b = board()

# function to initiatethe moving of a piece
def move_piece(type, current, new):
    x, y = ['b', 4], ['b', 5]
    if pawn.move(b.board, x, y, True):
        return b.update_board(x, y)
    return False