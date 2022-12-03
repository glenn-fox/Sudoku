"""
Glenn Fox

This file contains what is run, and compares two solving algorithms
"""


from solve import solve, draw_board, fast_solve
from timeit import default_timer as timer
from copy import deepcopy
from generator import create_board


def progress_bar(current, total, bar_length=20, string="Progress:"):
    """Function found on stack overflow created by user Avavind Voggu
    to create progress bar
    https://stackoverflow.com/questions/6169217/replace-console-output-in-python"""
    fraction = current / total

    arrow = int(fraction * bar_length - 1) * "-" + ">"
    padding = int(bar_length - len(arrow)) * " "

    ending = '\n' if current == total else "\r"

    print(f"{string} [{arrow}{padding}] {int(fraction*100)}%", end=ending)


# list to store multiple board objects for testing
boards = []

# get the number of clues to generate on each test board
clues = int(input("How many clues on each board do you want to test?(recommended 30): "))
# get how many boards to test for each algorithm
num_test_boards = int(input("How many boards to create for each test?(Recommended 50): "))

# create the test boards
for i in range(num_test_boards):
    boards.append(create_board(81-clues))
    progress_bar(len(boards), num_test_boards, string="Creating Boards:")

# make a copy of the boards so multiple algorithms can be tested with the same boards
boards_copy = deepcopy(boards)

# variable to store the times the solves took
times = []
boards_solved = 0

# my first solving algorithm start
for board in boards:
    start = timer()  # this is a test
    solved = solve(board)
    end = timer()

    boards_solved += 1
    progress_bar(boards_solved, num_test_boards, string="Regular Progress:")
    times.append(end-start)

average = sum(times) / len(times)
print("Regular solve average: " + str(average))

times = []
boards_solved = 0

for board in boards_copy:
    # start timer
    start = timer()
    # solve the board
    solved = fast_solve(board)
    # end timer
    end = timer()

    boards_solved += 1
    progress_bar(boards_solved, num_test_boards, string="Fast Solve Progress:")
    times.append(end-start)

average = sum(times) / len(times)
print("Fast solve average: " + str(average))


