#define board

from .pieces import p, r, t, b, q, k, P, R, T, B, Q, K
from .utils import coords_to_index

#class for the game board
class board:   
    def __init__(self):
        # set white side
        self.white = [P(['a', 2]), P(['b', 2]), P(['c', 2]), P(['d', 2]), P(['e', 2]), P(['f', 2]), P(['g', 2]), P(['h', 2]), 
        R(['a', 1]), T(['b', 1]), B(['c', 1]), Q(['d', 1]), K(['e', 1]), B(['f', 1]), T(['g', 1]), R(['h', 1])]
        # set the black side
        self.black = [p(['a', 7]), p(['b', 7]), p(['c', 7]), p(['d', 7]), p(['e', 7]), p(['f', 7]), p(['g', 7]), p(['h', 7]), 
        r(['a', 8]), t(['b', 8]), b(['c', 8]), q(['d', 8]), k(['e', 8]), b(['f', 8]), t(['g', 8]), r(['h', 8])]
        # set the initial board 
        self.board = [
            ['8  '] + self.black[8:16],
            ['7  '] + self.black[0:8],
            ['6  ', '. ', '. ', '. ', '. ' , '. ', '. ', '. ', '. '],
            ['5  ', '. ', '. ', '. ', '. ' , '. ', '. ', '. ', '. '],
            ['4  ', '. ', '. ', '. ', '. ' , '. ', '. ', '. ', '. '],
            ['3  ', '. ', '. ', '. ', '. ' , '. ', '. ', '. ', '. '],
            ['2  '] + self.white[0:8],
            ['1  '] + self.white[8:16],
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
        if new_location != '. ':
            if new_location in self.white:
                self.white.remove(new_location)
            elif new_location in self.black:
                self.black.remove(new_location)
            new_location = '. '
        self.board[new_index_y][new_index_x] = current_location
        self.board[current_index_y][current_index_x] = new_location
        self.draw()

