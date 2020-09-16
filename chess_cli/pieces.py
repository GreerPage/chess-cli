# define pieces

# class for pawn piece
class p():
    # return "piece" depending on color (capital = white)
    def draw(self, color):
        if color == 'w': return 'P '
        if color == 'b': return 'p '

    # logic piece moves — check if moves are valid
    def move(self, board, current, new):
        #lots of math
        pass

# class for rook piece
class r():
    # return "piece" depending on color (capital = white)
    def draw(self, color):
        if color == 'w': return 'R '
        if color == 'b': return 'r ' 

    # logic piece moves — check if moves are valid
    def move(self, board, current, new):
        #lots of math
        pass

# class for knight piece
class t():
    # return "piece" depending on color (capital = white)
    def draw(self, color):
        if color == 'w': return 'T '
        if color == 'b': return 't '

    # logic piece moves — check if moves are valid
    def move(self, board, current, new):
        #lots of math
        pass

# class for bishop piece
class b():
    # return "piece" depending on color (capital = white)
    def draw(self, color):
        if color == 'w': return 'B '
        if color == 'b': return 'b '

    # logic piece moves — check if moves are valid
    def move(self, board, current, new):
        #lots of math
        pass

# class for queen piece
class q():
    # return "piece" depending on color (capital = white)
    def draw(self, color):
        if color == 'w': return 'Q '
        if color == 'b': return 'q '

    # logic piece moves — check if moves are valid
    def move(self, board, current, new):
        #lots of math
        pass

# class for king piece
class k():
    # return "piece" depending on color (capital = white)
    def draw(self, color):
        if color == 'w': return 'K '
        if color == 'b': return 'k '

    # logic piece moves — check if moves are valid
    def move(self, board, current, new):
        #lots of math
        pass

pawn, rook, knight, bishop, king, queen = p(), r(), t(), b(), k(), q() 