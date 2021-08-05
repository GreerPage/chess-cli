# file for the command line interface (cli)
from .utils import coords_to_index, split_str, get_location, get_path_between_points
import readline

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
        prompt = "White's move: " if self.white else "Black's move: "
        try:
            command = input(prompt).split()
        except (KeyboardInterrupt, EOFError):
            exit()
        print()

        if len(command) == 0:
            self.board.draw()
            return

        if command[0].startswith('m') and len(command) == 3:
            c = split_str(command[1])
            n = split_str(command[2])
            try:
                piece = get_location(self.board.board, c)
            except ValueError:
                print('Invalid coordinates')
                return

            # move piece and change turn
            if self.white:
                if piece not in self.board.white:
                    print('You can only move a white piece')
                    return
                try:
                    if move_piece(self.board, c, n):
                        self.white = False
                    else:
                        print('Invalid move')
                except ValueError:
                    print('Invalid coordinates')
                    return
            else:
                if piece not in self.board.black:
                    print('You can only move a black piece')
                    return
                try:
                    if move_piece(self.board, c, n):
                        self.white = True
                    else:
                        print('Invalid move')
                except ValueError:
                    print('Invalid coordinates')
                    return
        
        elif command[0] == 'path':
            print(get_path_between_points([8, 0], [1, 7]))

        elif command[0] == 'q':
            exit()
            
        else:
            print('Invalid command')
