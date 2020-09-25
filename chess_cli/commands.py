# file for the command line interface (cli)
from .utils import coords_to_index, split_str, get_location, check_detection

# function to initiate a move
def move_piece(b, current, new):
    x, y = coords_to_index(current)
    piece = b.board[y][x]
    if piece.validate_move(b, current, new):
        b.update_board(current, new)
        return True
    return False

class game:
    def __init__(self, board):
        self.board = board
        self.white = True
    
    def cli(self):
        print()
        prompt = "White's move " if self.white else "Black's move "
        command = input(prompt)

        if command.startswith('m'):
            command = command.split()
            c = split_str(command[1])
            n = split_str(command[2])
            piece = get_location(self.board.board, c)
            if self.white:
                if piece not in self.board.white:
                    print('You can only move a white piece')
                    self.cli()
                move = move_piece(self.board, c, n)
                if move:
                    self.white = False
            else:
                if piece not in self.board.black:
                    print('You can only move a black piece')
                    self.cli()
                move = move_piece(self.board, c, n)
                if move:
                    self.white = True
        
        elif command == 'check':
            print(check_detection(self.board, self.board.white))

        elif command == 'q':
            exit()
            
        else:
            print('invalid command')

        self.cli()
    