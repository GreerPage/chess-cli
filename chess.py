#!/usr/bin/env python3
# file for starting game

from chess_cli import board, game

b = board()

def main():
    b.draw()
    g = game(b)
    g.cli()

if __name__=='__main__':
    main()