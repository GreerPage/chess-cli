# define pieces
from .utils import coords_to_index

# class for pawn piece
class p():
    # return "piece" depending on color (capital = white)
    def draw(self, color):
        if color == 'w': return 'P '
        if color == 'b': return 'p '

    # logic for piece moves — check if moves are valid
    def move(self, board, current, new, upper):
        current_x, current_y = coords_to_index(current)
        new_x, new_y = coords_to_index(new)

        if upper:
            if current_y - new_y < 0:
                return False 
            y_att_chg, start = current_y-1, 6
        else:
            if current_y - new_y > 0:
                return False 
            y_att_chg, start = current_y+1, 1

        if new_y == y_att_chg and current_x+1 == new_x:
            if board[y_att_chg][current_x+1] != '. ':
                if board[y_att_chg][current_x+1].isupper() == upper:
                    return False
                return True
            return False

        elif new_y == y_att_chg and current_x-1 == new_x:
            if board[y_att_chg][current_x-1] != '. ':
                if board[y_att_chg][current_x-1].isupper() == upper:
                    return False
                return True
            return False

        elif board[new_y][new_x] != '. ' or board[y_att_chg][current_x] != '. ':
            return False
        
        if current_y == start:
            if start == 2:
                if current_y-new_y == 2 or current_y-new_y == 1:
                    return True
                else:
                    return False
            
            elif start == 7:
                if current_y-new_y == -2 or current_y-new_y == -1:
                    return True
                else:
                    return False

        
        if current_x != new_x or current_y-new_y > 1 or current_y-new_y < -1: 
            return False
            

        return True


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