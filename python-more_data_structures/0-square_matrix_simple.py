#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """
    Computes the square value of all integers of a matrix
    Args:
        matrix: 2 dimensional array
    Returns:
        New matrix with all values squared
    """
    return [[x * x for x in row] for row in matrix]
