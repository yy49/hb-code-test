def reverse_list(l:list):
    """
    TODO: Reverse a list without using any built in functions

    The function should return a sorted list.
    Input l is a list which can contain any type of data.
    """
    # Return items by looping through index in reverse
    return [l[-index] for index in range(1, len(l) + 1)]


def solve_sudoku(matrix):
    """
    TODO: Write a programme to solve 9x9 Sudoku board.

    Sudoku is one of the most popular puzzle games of all time. The goal of Sudoku is to fill a 9×9 grid with numbers so that each row, column and 3×3 section contain all of the digits between 1 and 9. As a logic puzzle, Sudoku is also an excellent brain game.

    The input matrix is a 9x9 matrix. You need to write a program to solve it.
    """

    # Assuming all input matrixes are solvable with valid formatting
    # Assuming matrix is a 9x9 3d list: [[<row1>],[<row2>],...,[<row9>]], of number 1-9, blank cells are marked with value 0
    pass
