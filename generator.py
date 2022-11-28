from solve import possible, is_valid, draw_board, fast_solve, solve
from random import randrange


def create_board(blank):
    board = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    i = 0
    for i in [0, 3, 6]:

        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        col = i
        while col < i+3:
            row = i
            while row < i+3:
                board[col][row] = numbers.pop(randrange(len(numbers)))
                row += 1
            col += 1

    solve(board)

    blanks = 0

    while blanks < blank:
        x = randrange(0, 9)
        y = randrange(0, 9)

        if board[x][y] != 0:
            board[x][y] = 0
            blanks += 1

    return board
