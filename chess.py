from chess_cli import board, move_piece, right_down

b = board()

def main():
    b.draw()
    e = right_down(b.board, ['a', 8], 1)
    print(e)
    #print(move _piece('a', 's', 'a'))
    # calls for cli to activate and that will run from there ( this is all this file needs )

if __name__=='__main__':
    main()