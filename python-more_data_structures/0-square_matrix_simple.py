#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """Returns a new matrix where each value is squared.
    Args:
        matrix: 2D array of integers
    Returns:
        New matrix with squared values
    """
    return [[x ** 2 for x in row] for row in matrix]
