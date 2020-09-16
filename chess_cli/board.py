#define board

from .pieces import pawn, rook, bishop, knight, king, queen
from .utils import coords_to_index

#class for the game board
class board:   
    def __init__(self):
        # set the initial board 
        self.board = [
            ['8  ', rook.draw('b'), knight.draw('b'), bishop.draw('b'),   queen.draw('b'),   king.draw('b'),   bishop.draw('b'),   knight.draw('b'),   rook.draw('b')],
            ['7  ', pawn.draw('b'),   pawn.draw('b'),   pawn.draw('b'),   pawn.draw('b'),   pawn.draw('b'),   pawn.draw('b'),   pawn.draw('b'),   pawn.draw('b')],
            ['6  ', '. ', '. ', '. ', '. ' , '. ', '. ', '. ', '. '],
            ['5  ', '. ', '. ', '. ', '. ' , '. ', '. ', '. ', '. '],
            ['4  ', '. ', '. ', '. ', '. ' , '. ', '. ', '. ', '. '],
            ['3  ', '. ', '. ', '. ', '. ' , '. ', '. ', '. ', '. '],
            ['2  ', pawn.draw('w'),   pawn.draw('w'),   pawn.draw('w'),   pawn.draw('w'),   pawn.draw('w'),   pawn.draw('w'),   pawn.draw('w'),   pawn.draw('w')],
            ['1  ', rook.draw('w'),   knight.draw('w'),   bishop.draw('w'),   queen.draw('w'),   king.draw('w'),   bishop.draw('w'),   knight.draw('w'),   rook.draw('w')],
            ['', '', '', '', '', '', '', ''],
            ['   ', 'a ', 'b ', 'c ', 'd ', 'e ', 'f ', 'g ', 'h']
        ]
    
    # return string of current board to be printed
    def get_current_board(self):
        return self.board_to_string(self.board)

    # set the matrix representing the board into a string to print       
    def board_to_string(self, matrix):
        string_board = ''
        for row in matrix:
            row_string = ''
            for piece in row:
                row_string += piece
            row_string += '\n'
            string_board += row_string
        return string_board
    
    # update the board matrix when a move is determined to be valid
    def update_board(self, current, new):
        current_index_x, current_index_y  = coords_to_index(current)
        new_index_x, new_index_y = coords_to_index(new)
        current_location = self.board[current_index_y][current_index_x]
        new_location = self.board[new_index_y][new_index_x]
        self.board[new_index_y][new_index_x] = current_location
        self.board[current_index_y][current_index_x] = new_location
        return self.get_current_board()
