# define pieces
from .utils import coords_to_index, up, down, left, right, right_up, right_down, left_up, left_down, valid_vertical_horizontal_moves, l_up_right, l_up_left, l_down_left, l_down_right, knight_logic, valid_diagonal_moves, king_logic, check_detection, check_mate_detection

# white pawn
class P():
    def __init__(self, pos):
        self.moves = []
        self.passat = False
        self.position = pos

    def get_valid_moves(self, b, current):
        valid_moves = []
        cx, cy = coords_to_index(current)
        board = b.board
        side = b.white
        # move 2 spaces on first move
        if self.moves == [] and up(board, current, 2) == ['. ', '. ']:
            valid_moves.append([cx, cy-2])

        # attack
        if cx != 8:
            location = right_up(b.board, current, 1)[0]
            if location != '. ' and location not in side:
                valid_moves.append([cx+1, cy-1])

        location = left_up(b.board, current, 1)[0]
        if location != '. ' and location not in side:
            valid_moves.append([cx-1, cy-1])

        # one space forward
        if up(b.board, current, 1)[0] == '. ':
            valid_moves.append([cx, cy-1])

        return valid_moves

    def validate_move(self, b, current, new):
        position = coords_to_index(current)
        move_to = coords_to_index(new)
        valid_moves = self.get_valid_moves(b, current)    
        if move_to in valid_moves:
            self.position = new
            self.moves.append([position, move_to])
            return True
        return False
    
    def __str__(self):
        return 'P '
    
# black pawn
class p():
    def __init__(self, pos):
        self.moves = []
        self.passat = False
        self.position = pos
    
    def get_valid_moves(self, b, current):
        valid_moves = []
        cx, cy = coords_to_index(current)
        board = b.board
        side = b.black
        # move 2 spaces on first move
        if self.moves == [] and down(board, current, 2) == ['. ', '. ']:
            valid_moves.append([cx, cy+2])

        # attack
        if cx != 8:
            location = right_down(b.board, current, 1)[0]
            if location != '. ' and location not in side:
                valid_moves.append([cx+1, cy+1])

        location = left_down(b.board, current, 1)[0]
        if location != '. ' and location not in side:
            valid_moves.append([cx-1, cy+1])

        # one space forward
        if down(b.board, current, 1)[0] == '. ':
            valid_moves.append([cx, cy+1])
        
        return valid_moves

    def validate_move(self, b, current, new):
        position = coords_to_index(current)
        move_to = coords_to_index(new)
        valid_moves = self.get_valid_moves(b, current)    
        if move_to in valid_moves:
            self.position = new
            self.moves.append([position, move_to])
            return True
        return False

    def __str__(self):
        return 'p '

# white rook
class R():
    def __init__(self, pos):
        self.moves = []
        self.castle = True
        self.position = pos

    def get_valid_moves(self, b, current):
        return valid_vertical_horizontal_moves(b, current, b.white)

    def validate_move(self, b, current, new):
        position = coords_to_index(current)
        move_to = coords_to_index(new)
        self.position = move_to
        if self.get_valid_moves(b, current):
            self.position = new
            self.moves.append([position, move_to])
            self.castle = False
            return True
        return False
        

    def __str__(self):
        return 'R '

# black rook
class r():
    def __init__(self, pos):
        self.moves = []
        self.castle = True
        self.position = pos
    
    def get_valid_moves(self, b, current):
        return valid_vertical_horizontal_moves(b, current, b.black)

    def validate_move(self, b, current, new):
        position = coords_to_index(current)
        move_to = coords_to_index(new)
        if self.get_valid_moves(b, current):
            self.position = new
            self.moves.append([position, move_to])
            self.castle = False
            return True
        return False

    def __str__(self):
        return 'r '

# white knight
class T():
    def __init__(self, pos):
        self.moves = []
        self.position = pos
    
    def get_valid_moves(self, b, current):
        return knight_logic(b, current, b.white)
        
    def validate_move(self, b, current, new):
        position = coords_to_index(current)
        move_to = coords_to_index(new)
        valid_moves = self.get_valid_moves(b, current)
        if move_to in valid_moves:
            self.position = new
            self.moves.append([position, move_to])
            return True
        return False
        

    def __str__(self):
        return 'T '
        
    
class t():
    def __init__(self, pos):
        self.moves = []
        self.position = pos
    def get_valid_moves(self, b, current):
        return knight_logic(b, current, b.black)

    def validate_move(self, b, current, new):
        position = coords_to_index(current)
        move_to = coords_to_index(new)
        valid_moves = self.get_valid_moves(b, current)
        if move_to in valid_moves:
            self.position = move_to
            self.moves.append([position, move_to])
            return True
        return False

    def __str__(self):
        return 't '

# white bishop
class B():
    def __init__(self, pos):
        self.moves = []
        self.position = pos
    def get_valid_moves(self, b, current):
        return valid_diagonal_moves(b, current, b.white)

    def validate_move(self, b, current, new):
        position = coords_to_index(current)
        move_to = coords_to_index(new)
        valid = self.get_valid_moves(b, current)
        if valid:
            self.position = new
            self.moves.append([position, move_to])
            return True
        return False

    def __str__(self):
        return 'B '
    
# black bishop
class b():
    def __init__(self, pos):
        self.moves = []
        self.position = pos
    
    def get_valid_moves(self, b, current):
        return valid_diagonal_moves(b, current, b.black)

    def validate_move(self, b, current, new):
        position = coords_to_index(current)
        move_to = coords_to_index(new)
        valid = self.get_valid_moves(b, current)
        if valid:
            self.position = new
            self.moves.append([position, move_to])
            return True
        return False

    def __str__(self):
        return 'b '

# white queen 
class Q():
    def __init__(self, pos):
        self.moves = []
        self.position = pos
    
    def get_valid_moves(self, b, current):    
        valid_moves = valid_diagonal_moves(b, current, b.white)
        valid_moves += valid_vertical_horizontal_moves(b, current, b.white)
        return valid_moves

    def validate_move(self, b, current, new):
        position = coords_to_index(current)
        move_to = coords_to_index(new)
        if move_to in self.get_valid_moves(b, current):
            self.position = new
            self.moves.append([position, move_to])
            return True
        return False

    def __str__(self):
        return 'Q '

# black queen
class q():
    def __init__(self, pos):
        self.moves = []
        self.position = pos
    
    def get_valid_moves(self, b, current):    
        valid_moves = valid_diagonal_moves(b, current, b.black)
        valid_moves += valid_vertical_horizontal_moves(b, current, b.black)
        return valid_moves

    def validate_move(self, b, current, new):
        position = coords_to_index(current)
        move_to = coords_to_index(new)
        if move_to in self.get_valid_moves(b, current):
            self.position = new
            self.moves.append([position, move_to])
            return True
        return False

    def __str__(self):
        return 'q '

# white king
class K():
    def __init__(self, pos):
        self.moves = []
        self.position = pos
        self.check = False
    
    def get_valid_moves(self, b, current):
        return king_logic(b, current, b.white)

    def validate_move(self, b, current, new):
        position = coords_to_index(current)
        move_to = coords_to_index(new)
        valid_moves = self.get_valid_moves(b, current)
        if move_to in check_detection(b, b.black):
            return False
        if move_to in valid_moves:
            self.position = new
            self.moves.append([position, move_to])
            return True
        return False

    def __str__(self):
        return 'K '

# black king
class k():
    def __init__(self, pos):
        self.moves = []
        self.position = pos
        self.check = False
    
    def get_valid_moves(self, b, current):
        return king_logic(b, current, b.black)

    def validate_move(self, b, current, new):
        position = coords_to_index(current)
        move_to = coords_to_index(new)
        #if move_to in check_detection(b, b.white):
            #return False
        print(check_mate_detection(b, b.black, check_detection(b, b.black)[0], self.position))
        valid_moves = self.get_valid_moves(b, current)
        if move_to in valid_moves:
            self.position = new
            self.moves.append([position, move_to])
            return True
        return False

    def __str__(self):
        return 'k '

