# file for the command line interface (cli)
from .board import board

b = board()

# function to initiatethe moving of a piece
def move_piece(type, current, new):
    return b.update_board(['a', 2], ['e', 8])
