#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        square = list(map(lambda x: x**2, row))
        new_matrix.append(square)
    return new_matrix
