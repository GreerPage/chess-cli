#!/usr/bin/env python3
# file for starting game

from os import environ
from chess_cli import board, game

def main():
    color = True
    if 'NO_COLOR' in environ:
        color = False
    b = board(color=color)
    b.draw()
    g = game(b)
    while True:
        g.cli()

if __name__ == '__main__':
    main()
