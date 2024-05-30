def reverse_list(l:list):
    """
    TODO: Reverse a list without using any built in functions

    The function should return a sorted list.
    Input l is a list which can contain any type of data.
    """
    # Handle edge cases
    if l is None or len(l) <= 1:
        return l
    # Return items by looping through index in reverse
    return [l[-index] for index in range(1, len(l) + 1)]


def solve_sudoku(matrix):
    """
    TODO: Write a programme to solve 9x9 Sudoku board.

    Sudoku is one of the most popular puzzle games of all time. The goal of Sudoku is to fill a 9×9 grid with numbers so that each row, column and 3×3 section contain all of the digits between 1 and 9. As a logic puzzle, Sudoku is also an excellent brain game.

    The input matrix is a 9x9 matrix. You need to write a program to solve it.

    Test data:                                  Solved:
    [                                           [
        [0, 0, 0, 1, 2, 3, 0, 8, 0],                [4, 7, 9, 1, 2, 3, 5, 8, 6],
        [1, 0, 0, 0, 0, 0, 0, 3, 7],                [1, 6, 2, 5, 8, 9, 4, 3, 7],
        [0, 0, 8, 7, 4, 6, 9, 0, 0],                [5, 3, 8, 7, 4, 6, 9, 1, 2],
        [3, 0, 5, 0, 0, 0, 6, 2, 9],                [3, 4, 5, 8, 1, 7, 6, 2, 9],
        [7, 2, 6, 0, 0, 0, 0, 0, 0],                [7, 2, 6, 3, 9, 4, 1, 5, 8],
        [8, 0, 1, 0, 0, 0, 3, 0, 4],                [8, 9, 1, 2, 6, 5, 3, 7, 4],
        [0, 0, 7, 9, 0, 0, 2, 0, 3],                [6, 8, 7, 9, 5, 1, 2, 4, 3],
        [9, 0, 3, 4, 7, 0, 0, 6, 5],                [9, 1, 3, 4, 7, 2, 8, 6, 5],
        [0, 5, 0, 6, 0, 8, 0, 0, 1]                 [2, 5, 4, 6, 3, 8, 7, 9, 1]
    ]                                           ]
    """
    # Assuming all input matrixes are solvable with valid formatting
    # Assuming matrix is a 9x9 3d list: [[<row1>],[<row2>],...,[<row9>]], of number 1-9, blank cells are marked with value 0

    # Method for checking if a cell value is valid against row/column/section
    # By checking if the value is already filled
    def isValid(matrix, value, row, column):
        # Row
        if value in matrix[row]:
            return False

        # Column
        for r in range(9):
            if matrix[r][column] == value:
                return False

        # Locate the top-left cell of the 3x3 section
        # Where the cell being validated is located at
        sectionR = row // 3 * 3
        sectionC = column // 3 * 3

        # Section
        for r in range(sectionR, sectionR + 3):
            for c in range(sectionC, sectionC + 3):
                if matrix[r][c] == value:
                    return False

        return True

    # Find solutions with backtrack, always begin from the last filled cell
    def backtrack(matrix, row, column):
        # Loop through the matrix
        while row < 9:
            while column < 9:
                # Only check for blank cells
                if matrix[row][column] == 0:
                    # Get next cell in order
                    nextRow = row + 1 if column == 8 else row
                    nextCol = column + 1 if column < 8 else 0

                    # Validate through all possible values
                    for value in range(1, 10):
                        if isValid(matrix, value, row, column):
                            # Fill in cell with valid value
                            matrix[row][column] = value

                            # Recursively check from next cell and return true if a solution is found
                            if backtrack(matrix, nextRow, nextCol):
                                return True

                            # Backtrack and check for next possible value
                            matrix[row][column] = 0

                    # If all possible values are not valid, return False
                    return False

                column += 1

            # Reset column count for new row
            column = 0
            row += 1

        # Return true if all cells are checked and filled
        return True

    backtrack(matrix, 0, 0)
    return matrix
