# define pieces
from .utils import coords_to_index

# class for pawn piece
class p():
    # return "piece" depending on color (capital = white)
    def draw(self, color):
        if color == 'w': return 'P '
        if color == 'b': return 'p '

    # logic for piece moves — check if moves are (valid pawns are hard >::( too many rules also this function is way too long fml)
    def move(self, board, current, new, upper):
        current_x, current_y = coords_to_index(current)
        new_x, new_y = coords_to_index(new)
        # set vars accoring to color upper==True: white
        if upper:
            # no backwards
            if current_y - new_y < 0:
                return False 
            y_att_chg, start = current_y-1, 6
        else:
            # no backwards
            if current_y - new_y > 0:
                return False 
            y_att_chg, start = current_y+1, 1
        # allowing pawns to attack diagonally in both directions
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

        # check if there are pieces in destination or path
        if board[new_y][new_x] != '. ' or board[y_att_chg][current_x] != '. ':
            return False
        # allow pawns to maovetwo places at first move
        if current_y == start:
            # for white
            if start == 6:
                if current_y-new_y == 2 or current_y-new_y == 1:
                    return True
                else:
                    return False
            #for black
            elif start == 1:
                if current_y-new_y == -2 or current_y-new_y == -1:
                    return True
                else:
                    return False

        # not let pawns move 2 spaces after first move
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
    def move(self, board, current, new, upper):
        current_x, current_y = coords_to_index(current)
        new_x, new_y = coords_to_index(new)
        # prevent diagonal moves
        if current_x != new_x and current_y != new_y:
            return False
        # find pieces in path
        #horizontal move
        if current_x != new_x:
            if current_x < new_x: b, s = new_x, current_x
            if new_x < current_x: b, s = current_x, new_x
            for i in range(s+1, b+1):
                if board[current_y][i] != '. ':
                    return False
        return True

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