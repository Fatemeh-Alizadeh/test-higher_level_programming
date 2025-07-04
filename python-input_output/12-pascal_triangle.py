#!/usr/bin/python3
"""
Returns a list of lists of integers representing Pascal's triangle of n rows.
If n <= 0, returns an empty list.
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing Pascal's triangle of n rows.
    If n <= 0, returns an empty list.
    """
    if n <= 0:
        return []

    triangle = []
    for row_num in range(n):
        row = [1]
        if triangle:
            last_row = triangle[-1]
            for i in range(1, row_num):
                row.append(last_row[i - 1] + last_row[i])
            if row_num > 0:
                row.append(1)
        triangle.append(row)

    return triangle
