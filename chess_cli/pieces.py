# define pieces
from .utils import coords_to_index, up, down, left, right, right_up, right_down, left_up, left_down, valid_vertical_horizontal_moves, l_up_right, l_up_left, l_down_left, l_down_right, knight_logic

# white pawn
class P():
    def __init__(self):
        self.moves = []
        self.passat = False

    def validate_move(self, b, current, new):
        valid_moves = []
        cx, cy = coords_to_index(current)
        position = coords_to_index(current)
        move_to = coords_to_index(new)
        board = b.board
        side = b.white
        # move 2 spaces on first move
        if self.moves == [] and up(board, current, 2) == ['. ', '. ']:
            valid_moves.append([cx, cy-2])

        # attack
        location = right_up(b.board, current, 1)[0]
        if location != '. ' and location not in side:
            valid_moves.append([cx+1, cy-1])

        location = left_up(b.board, current, 1)[0]
        if location != '. ' and location not in side:
            valid_moves.append([cx-1, cy-1])

        # one space forward
        if up(b.board, current, 1)[0] == '. ':
            valid_moves.append([cx, cy-1])
            
        if move_to in valid_moves:
            self.moves.append([position, move_to])
            return True

        return False
    
    def __str__(self):
        return 'P '
    

# black pawn
class p():
    def __init__(self):
        self.moves = []
        self.passat = False
    
    def validate_move(self, b, current, new):
        valid_moves = []
        cx, cy = coords_to_index(current)
        position = coords_to_index(current)
        move_to = coords_to_index(new)
        board = b.board
        side = b.black
        # move 2 spaces on first move
        if self.moves == [] and down(board, current, 2) == ['. ', '. ']:
            valid_moves.append([cx, cy+2])

        # attack
        location = right_down(b.board, current, 1)[0]
        if location != '. ' and location not in side:
            valid_moves.append([cx+1, cy+1])

        location = left_down(b.board, current, 1)[0]
        if location != '. ' and location not in side:
            valid_moves.append([cx-1, cy+1])

        # one space forward
        if down(b.board, current, 1)[0] == '. ':
            valid_moves.append([cx, cy+1])
            
        if move_to in valid_moves:
            self.moves.append([position, move_to])
            return True

        return False

    def __str__(self):
        return 'p '


# white rook
class R():
    def __init__(self):
        self.moves = []
        self.castle = True
    
    def validate_move(self, b, current, new):
        position = coords_to_index(current)
        move_to = coords_to_index(new)
        if valid_vertical_horizontal_moves(b, current, new, b.white):
            self.moves.append([position, move_to])
            self.castle = False
            return True
        return False
        

    def __str__(self):
        return 'R '


# black rook
class r():
    def __init__(self):
        self.moves = []
        self.castle = True
    
    def validate_move(self, b, current, new):
        position = coords_to_index(current)
        move_to = coords_to_index(new)
        if valid_vertical_horizontal_moves(b, current, new, b.black):
            self.moves.append([position, move_to])
            self.castle = False
            return True
        return False

    def __str__(self):
        return 'r '

    

# white knight
class T():
    def __init__(self):
        self.moves = []
    
    def validate_move(self, b, current, new):
        position = coords_to_index(current)
        move_to = coords_to_index(new)
        board = b.board
        side = b.white
        valid_moves = knight_logic(board, current, side)
        if move_to in valid_moves:
            self.moves.append([position, move_to])
            return True
        return False
        

    def __str__(self):
        return 'T '
    
   


# black knight.
class t():
    def __init__(self):
        self.moves = []
    
    def validate_move(self, b, current, new):
        position = coords_to_index(current)
        move_to = coords_to_index(new)
        board = b.board
        side = b.black
        valid_moves = knight_logic(board, current, side)
        if move_to in valid_moves:
            self.moves.append([position, move_to])
            return True
        return False

    def __str__(self):
        return 't '

    


# white bishop
class B():
    def __init__(self):
        self.moves = []
    
    def __str__(self):
        return 'B '
    
    

# black bishop
class b():
    def __init__(self):
        self.moves = []
    
    def __str__(self):
        return 'b '

    


# white queen 
class Q():
    def __init__(self):
        self.moves = []
    
    def __str__(self):
        return 'Q '


# black queen
class q():
    def __init__(self):
        self.moves = []
    
    def __str__(self):
        return 'q '

   

# white king
class K():
    def __init__(self):
        self.moves = []
    
    def __str__(self):
        return 'K '

   

# black king
class k():
    def __init__(self):
        self.moves = []
    
    def __str__(self):
        return 'k '

