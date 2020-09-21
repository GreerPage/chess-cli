from chess_cli import board, move_piece
b = board()

def main():
    b.draw()
    print(move_piece('a', 's', 'a'))
    # calls for cli to activate and that will run from there ( this is all this file needs )

if __name__=='__main__':
    main()