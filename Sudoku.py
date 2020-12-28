# Sudoku Board to be solved
import platform
import sys
board = [[0, 0, 0, 0, 4, 7, 0, 1, 6],
         [5, 0, 1, 0, 0, 0, 7, 0, 0],
         [0, 6, 3, 0, 2, 0, 8, 0, 0],
         [0, 0, 0, 6, 3, 1, 0, 2, 7],
         [0, 0, 7, 9, 0, 2, 4, 0, 0],
         [3, 9, 0, 4, 7, 5, 0, 0, 0],
         [0, 0, 5, 0, 9, 0, 2, 6, 0],
         [0, 0, 6, 0, 0, 0, 5, 0, 8],
         [2, 8, 0, 3, 5, 0, 0, 0, 0]]


# Determines whether we can input a valid number (1-9)
# Follows the constraints of a Sudoku Board
# Valid Row, Valid Column, Valid Subgrid
def valid_choice(row, column, choice):
    # Row
    for element in range(0, 9):
        if element != column:
            if board[row][element] == choice:
                return False

    # Column
    for row_index in range(0, 9):
        if row_index != row:
            if board[row_index][column] == choice:
                return False

    # Grids #1-3
    if row < 3:
        if column < 3:
            temp_row = 0
            temp_column = 0

        if column > 2 and column < 6:
            temp_row = 0
            temp_column = 3

        if column > 5 and column < 9:
            temp_row = 0
            temp_column = 6

    # Grids #3-6
    if row > 2 and row < 6:

        if column < 3:
            temp_row = 3
            temp_column = 0

        if column > 2 and column < 6:
            temp_row = 3
            temp_column = 3

        if column > 5 and column < 9:
            temp_row = 3
            temp_column = 6

    # Grids #6-9
    if row > 5 and row < 9:

        if column < 3:
            temp_row = 6
            temp_column = 0

        if column > 2 and column < 6:
            temp_row = 6
            temp_column = 3

        if column > 5 and column < 9:
            temp_row = 6
            temp_column = 6

    # Based of the Grid number, we can loop through the subgrid
    for row_index in range(temp_row, temp_row + 3):
        for col_index in range(temp_column, temp_column + 3):
            if row_index != row or col_index != column:
                if board[row_index][col_index] == choice:
                    return False

    # Returns True if we satisfy all constraints
    return True

# Determines whether a cell is not empty


def empty_cell(row, column):
    # If a cell has a value other than 0, return False
    if board[row][column] != 0:
        return False

# Uses the Backtracking algorithm to solve the board


def solution_board(row, column):
    # Base Case
    # Board is full meaning we filled the entire board
    if column == 9 and row == 8:
        return True

    # Once we reach the end of the row, start a new row by updating the row, and setting the column to zero
    if column == 9:
        row = row + 1
        column = 0

    # Checks if a cell is not empty
    if empty_cell(row, column) == False:
        # Recurses on the cells that don't need to be filled
        if solution_board(row, column + 1):
            # Ends each recursive call
            return True

    # Exploration on possibilities for each cell #1-9
    for choice in range(1, 10):
        # If we have a valid element, put it in the cell
        if valid_choice(row, column, choice):
            board[row][column] = choice
            # Recurses on the board, till we fill it up
            if solution_board(row, column + 1):
                # Ends each recursive call
                return True
            # If we dont have a valid choice for a previous recursive call
            # We backtrack, thus setting the previous cell to zero, and explore on further possibilities
            board[row][column] = 0

    # Returns False if we don't have a valid choice
    return False


# MAIN
# Calls the function to solve the Sudoku Board
solution_board(0, 0)
# Prints out the board
for row in range(0, 9):
    for column in range(0, 9):
        if (column + 1) % 3 == 0:
            if column == 8:
                print(board[row][column])
                if (row + 1) % 3 == 0:
                    print("---------------------")
                break
            print(board[row][column], end=' | ')
        else:
            print(board[row][column], end=' ')
