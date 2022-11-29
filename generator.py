"""
Glenn Fox

This file contains the function to generate sudoku boards
"""

from solve import possible, is_valid, draw_board, fast_solve, solve
from random import randrange


def create_board(blank):
    """Takes in an integer blank, and returns a sudoku board with that number of blank cells"""
    board = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0]]

    # fill the big squares in a diagonal with numbers
    for i in [0, 3, 6]:
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        col = i
        while col < i+3:
            row = i
            while row < i+3:
                board[col][row] = numbers.pop(randrange(len(numbers)))
                row += 1
            col += 1

    # Fill the rest with the board using the solve function
    solve(board)

    blanks = 0

    # make random cells blank
    while blanks < blank:
        x = randrange(0, 9)
        y = randrange(0, 9)

        if board[x][y] != 0:
            board[x][y] = 0
            blanks += 1

    return board
