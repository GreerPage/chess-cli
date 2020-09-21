#define board

from .pieces import p, r, t, b, q, k, P, R, T, B, Q, K
from .utils import coords_to_index

#class for the game board
class board:   
    def __init__(self):
        # set the initial board 
        self.board = [
            ['8  ', r(), t(), b(), q(), k(), b(), t(), r()],
            ['7  ', p(), p(), p(), p(), p(), p(), p(), p()],
            ['6  ', '. ', '. ', '. ', '. ' , '. ', '. ', '. ', '. '],
            ['5  ', '. ', '. ', '. ', '. ' , '. ', '. ', '. ', '. '],
            ['4  ', '. ', '. ', '. ', '. ' , '. ', '. ', '. ', '. '],
            ['3  ', '. ', '. ', '. ', '. ' , '. ', '. ', '. ', '. '],
            ['2  ', P(), P(), P(), P(), P(), P(), P(), P()],
            ['1  ', R(), T(), B(), Q(), K(), 'B()', T(), R()],
            ['', '', '', '', '', '', '', ''],
            ['   ', 'a ', 'b ', 'c ', 'd ', 'e ', 'f ', 'g ', 'h']
        ]
    
    # draw board
    def draw(self):
        for row in self.board:
            for piece in row:
                print(piece, end='')
            print()
    
    # update the board matrix when a move is determined to be valid
    def update_board(self, current, new):
        current_index_x, current_index_y  = coords_to_index(current)
        new_index_x, new_index_y = coords_to_index(new)
        current_location = self.board[current_index_y][current_index_x]
        new_location = self.board[new_index_y][new_index_x]
        self.board[new_index_y][new_index_x] = current_location
        self.board[current_index_y][current_index_x] = new_location
        self.draw()

