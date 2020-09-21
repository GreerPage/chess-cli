# file for the command line interface (cli)
from .utils import coords_to_index

# function to initiate a move
def move_piece(b, current, new):
    x, y = coords_to_index(current)
    piece = b.board[y][x]
    piece.validate_move(b, current, new)