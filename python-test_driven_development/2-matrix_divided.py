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
    if (not isinstance(matrix, list) or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    row_length = None
    for row in matrix:
        if row_length is None:
            row_length = len(row)
        elif len(row) != row_length:
            raise TypeError(
                "Each row of the matrix must have the same size")

        for item in row:
            if not isinstance(item, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats"
                )

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [
        [round(item / div, 2)
         for item in row]
        for row in matrix]

