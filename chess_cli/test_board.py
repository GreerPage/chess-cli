# file for testing board states (i hate it too)

class test_board:
    def __init__(self, matrix):
        self.board = matrix
    
    def test(self, side, move):
        p = 'p ' if side == 'white' else 'P '
        if move[0] < 8 and move[1] < 7:
            self.board[move[1]][move[0]] = p
        return self.board