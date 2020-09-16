# file for the command line interface (cli)
from .board import board
from .pieces import pawn, rook, knight, bishop, queen, king

b = board()

# function to initiatethe moving of a piece
def move_piece(type, current, new):
    return pawn.move(b.board, ['b', 2], ['a', 2])
