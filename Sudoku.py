def is_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0: return (i, j) # Empty Coordinates: col, row
    return None

def is_valid(board, number, position):
    #=> Check Rows <=#
    for i in range(len(board)):
        if board[position[0]][i] == number and position[1] != i: return False
    #=> Check Columns <=#
    for i in range(len(board)):
        if board[i][position[1]] == number and position[0] != i: return False
    #=> Check Boxes <=#
    xbox = position[1] // 3
    ybox = position[0] // 3
    for i in range(ybox * 3, ybox * 3 + 3):
        for j in range(xbox * 3, xbox * 3 + 3):
            if board[i][j] == number and (i, j) != position: return False
    return True

def backtrack_solve(board):
    empty = is_empty(board)
    if not empty: return True
    else: row, col = empty
    for i in range(1, 10):
        if is_valid(board, i, (row, col)):
            board[row][col] = i
            if backtrack_solve(board): return True
            board[row][col] = 0
    return False

def checkio(board):
    backtrack_solve(board)
    return board
