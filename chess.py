from chess_cli import board, move_piece, left
b = board()

def main():
    b.draw()
    e = left(b.board, ['h', 1], 7)
    print(e)
    #print(move _piece('a', 's', 'a'))
    # calls for cli to activate and that will run from there ( this is all this file needs )

if __name__=='__main__':
    main()