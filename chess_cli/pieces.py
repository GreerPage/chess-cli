# define pieces

# class for pawn piece
class p():
    def draw(self, color):
        if color == 'w': return 'P '
        if color == 'b': return 'p '

    def move(self, board, current, new):
        #lots of math
        pass

# class for rook piece
class r():
    def draw(self, color):
        if color == 'w': return 'R '
        if color == 'b': return 'r ' 

    def move(self, board, current, new):
        #lots of math
        pass

# class for knight piece
class t():
    def draw(self, color):
        if color == 'w': return 'T '
        if color == 'b': return 't '

    def move(self, board, current, new):
        #lots of math
        pass

# class for bishop piece
class b():
    def draw(self, color):
        if color == 'w': return 'B '
        if color == 'b': return 'b '

    def move(self, board, current, new):
        #lots of math
        pass

# class for queen piece
class q():
    def draw(self, color):
        if color == 'w': return 'Q '
        if color == 'b': return 'q '

    def move(self, board, current, new):
        #lots of math
        pass

# class for king piece
class k():
    def draw(self, color):
        if color == 'w': return 'K '
        if color == 'b': return 'k '

    def move(self, board, current, new):
        #lots of math
        pass

pawn, rook, knight, bishop, king, queen = p(), r(), t(), b(), k(), q() 