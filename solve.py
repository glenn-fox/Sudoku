"""
Glenn Fox

This file stores functions to solve sudoku boards
"""


def draw_board(board):
    """Function draws a sudoku board to the console"""
    for i, line in enumerate(board):
        for j, item in enumerate(line):
            print(item, end=" ")
            if j in [2, 5]:
                print("|", end=" ")
        print("")
        if i in [2, 5]:
            print("------+-------+------")
    print("")


def possible(board, pos, num):
    """Function determines if a number is a possible move for a position on a board.

    Parameters:
    board (array): array that holds the board information
    pos (tuple): position on the board (y, x)
    num (int): number to be tested

    Returns bool
    """
    # pos is (y, x)
    y = pos[0]
    x = pos[1]

    # check row
    for item in board[y]:
        if item == num:
            return False

    # check column
    for row in board:
        if row[x] == num:
            return False

    # check square
    box_x = (x // 3) * 3
    box_y = (y // 3) * 3
    for i in list(range(box_y, box_y+3)):
        for j in list(range(box_x, box_x+3)):
            if board[i][j] == num:
                return False

    return True


def is_valid(board):
    """Function checks if board is valid by checking board for duplicate numbers in rows, columns, and squares"""

    # check horizontal lines
    for line in board:
        numbers = []
        for number in line:
            # add numbers in line to list
            # if there are more than one of any number except 0 then the line is not valid
            if number in numbers and number != 0:
                return False
            elif number not in numbers:
                numbers.append(number)

    # check vertical lines
    indexes = list(range(0, 9))
    for index in indexes:
        numbers = []
        for line in board:
            number = line[index]
            if number in numbers and number != 0:
                return False
            elif number not in numbers:
                numbers.append(number)

    # Check squares
    start_i = 0
    start_j = 0
    while start_j <= 6:
        while start_i <= 6:
            numbers = []
            for i in list(range(start_i, start_i + 3)):
                for j in list(range(start_j, start_j + 3)):
                    number = board[i][j]
                    if number in numbers and number != 0:
                        return False
                    elif number not in numbers:
                        numbers.append(number)
            start_i += 3
        start_j += 3
        start_i = 0

    return True


def completed(board):
    """Function checks if board is valid and there are no blank cells"""

    # make sure the board is valid
    if is_valid(board):
        # make sure there are no 0s (blanks) in the board
        for line in board:
            if 0 not in line:
                continue
            else:
                return False
        return True
    return False


def solve(board):
    """Simple solving algorithm that starts with first blank cell"""
    for i in list(range(0, 9)):
        for j in list(range(0, 9)):
            if board[i][j] == 0:
                for testNum in list(range(1, 10)):
                    if possible(board, (i, j), testNum):
                        board[i][j] = testNum
                        board = solve(board)
                        if completed(board):
                            return board
                    if testNum == 9:
                        board[i][j] = 0
                        return board
    return board


def fast_solve(board, moves=[]):
    """Solve algorithm that starts with cell with the least number of possible moves"""
    # check if board is complete
    complete = completed(board)

    if len(moves) > 0 and not complete:
        # iterate through moves
        for coords, move_list in moves:
            if board[coords[0]][coords[1]] == 0:
                break
        for item in move_list:
            if possible(board, coords, item):
                board[coords[0]][coords[1]] = item
                board = fast_solve(board, moves)
                if completed(board):
                    return board
        # if not completed(board):
        board[coords[0]][coords[1]] = 0
        return board

    elif len(moves) == 0 and not complete:
        # get the move list
        for i in list(range(0, 9)):
            for j in list(range(0, 9)):
                item_list = []
                if board[i][j] == 0:
                    # do stuff
                    for testNum in list(range(1, 10)):
                        if possible(board, (i, j), testNum):
                            item_list.append(testNum)
                    moves.append([(i, j), item_list])
                else:
                    pass

        moves.sort(key=inner_length)
        fast_solve(board, moves)
    return board


def inner_length(move):
    """Function that returns the length of the second list in a list of lists"""
    return len(move[1])

