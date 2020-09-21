# file for the command line interface (cli)
from .utils import coords_to_index, split_str

# function to initiate a move
def move_piece(b, current, new):
    x, y = coords_to_index(current)
    piece = b.board[y][x]
    if piece.validate_move(b, current, new):
        b.update_board(current, new)

class game:
    def __init__(self, board):
        self.board = board
        self.white = True
    
    def cli(self):
        print()
        command = input('Enter a command ')

        if command.startswith('m'):
            command = command.split()
            c = split_str(command[1])
            n = split_str(command[2])
            move_piece(self.board, c, n)
        
        elif command == 'q':
            exit()
            
        else:
            print('invalid command')

        self.cli()
    