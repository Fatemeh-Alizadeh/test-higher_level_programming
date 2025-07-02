#!/usr/bin/python3
"""
This module provides a function that divides all elements of a matrix.
"""

def matrix_divided(matrix, div):
    """
        Divides all elements of a matrix by a number.

        Args:
            matrix (list of lists)
            div (int or float)

        Returns:
            list of lists: A new matrix with all elements divided and rounded.

        Raises:
            TypeError: If matrix is not a list of lists of integers/floats,
                       or if the rows are not the same size,
                       or if div is not a number.
            ZeroDivisionError: If div is 0.
        """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row-lengh = 0


    new_matrix = [[]]
    for row in matrix:
        new_row = []
        for num in row:
            new_row.append(round(num / div, 2))
        new_matrix.append(new_row)
    return new_matrix
