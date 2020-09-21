from chess_cli import board, move_piece, left_down
b = board()

def main():
    b.draw()
    e = left_down(b.board, ['h', 8], 3)
    print(e)
    #print(move _piece('a', 's', 'a'))
    # calls for cli to activate and that will run from there ( this is all this file needs )

if __name__=='__main__':
    main()