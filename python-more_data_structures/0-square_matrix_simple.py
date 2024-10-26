#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """
    Computes the square value of all integers of a matrix.
    
    Args:
        matrix: A 2 dimensional array of integers
        
    Returns:
        A new matrix with all values squared
    """
    return [[x**2 for x in row] for row in matrix]
