# file for the command line interface (cli)
from .board import board
from .pieces import p, r, t, b, q, k, P, R, T, B, Q, K

b = board()

# function to initiatethe moving of a piece
def move_piece(type, current, new):
    x, y = ['a', 5], ['a', 3]
    if rook.move(b.board, x, y, False):
        return b.update_board(x, y)
    return False