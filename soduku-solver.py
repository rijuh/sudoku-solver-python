def check(board, row, col, n):
    # CHECKING FOR ROW
    for i in range(9):
        if board[row][i] == n:
            return False

    # CHECKING FOR COLUMN
    for i in range(9):
        if board[i][col] == n:
            return False

    # CHECKING FOR THE GRID
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == n:
                return False
    return True


def solver(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for n in range(1, 10):
                    if check(board, row, col, n):
                        board[row][col] = n
                        if solver(board):
                            return True
                        board[row][col] = 0
                return False
    return True


def print_board(board):
    for row in board:
        print(" ".join(map(str, row)))


print("Enter the row by space-separated values: \n")
# YOU CAN UNCOMMENT THIS GIVE INPUT ANY BOARD
# board = [[int(value) for value in input("").split()] for i in range(9)]
board = [
    [3, 0, 6, 5, 0, 8, 4, 0, 0],
    [5, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 8, 7, 0, 0, 0, 0, 3, 1],
    [0, 0, 3, 0, 1, 0, 0, 8, 0],
    [9, 0, 0, 8, 6, 3, 0, 0, 5],
    [0, 5, 0, 0, 9, 0, 6, 0, 0],
    [1, 3, 0, 0, 0, 0, 2, 5, 0],
    [0, 0, 0, 0, 0, 0, 0, 7, 4],
    [0, 0, 5, 2, 0, 6, 3, 0, 0]
]
print_board(board)
print("\n solved \n")
if solver(board):
    print_board(board)