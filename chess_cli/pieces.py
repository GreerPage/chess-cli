# define pieces
from .utils import coords_to_index, global_move_checker

# class for pawn piece
class p():
    # return "piece" depending on color (capital = white)
    def draw(self, color):
        if color == 'w': return 'P '
        if color == 'b': return 'p '

    # logic for piece moves — check if moves are valid
    def move(self, board, current, new):
        current_x, current_y = coords_to_index(current)
        new_x, new_y = coords_to_index(new)
        return global_move_checker(current_x, current_y, new_x, new_y, board)

# class for rook piece
class r():
    # return "piece" depending on color (capital = white)
    def draw(self, color):
        if color == 'w': return 'R '
        if color == 'b': return 'r ' 

    # logic for piece moves — check if moves are valid
    def move(self, board, current, new):
        #lots of math
        pass

# class for knight piece
class t():
    # return "piece" depending on color (capital = white)
    def draw(self, color):
        if color == 'w': return 'T '
        if color == 'b': return 't '

    # logic for piece moves — check if moves are valid
    def move(self, board, current, new):
        #lots of math
        pass

# class for bishop piece
class b():
    # return "piece" depending on color (capital = white)
    def draw(self, color):
        if color == 'w': return 'B '
        if color == 'b': return 'b '

    # logic for piece moves — check if moves are valid
    def move(self, board, current, new):
        #lots of math
        pass

# class for queen piece
class q():
    # return "piece" depending on color (capital = white)
    def draw(self, color):
        if color == 'w': return 'Q '
        if color == 'b': return 'q '

    # logic for piece moves — check if moves are valid
    def move(self, board, current, new):
        #lots of math
        pass

# class for king piece
class k():
    # return "piece" depending on color (capital = white)
    def draw(self, color):
        if color == 'w': return 'K '
        if color == 'b': return 'k '

    # logic for piece moves — check if moves are valid
    def move(self, board, current, new):
        #lots of math
        pass

pawn, rook, knight, bishop, king, queen = p(), r(), t(), b(), k(), q() 