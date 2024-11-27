#!/usr/bin/python3
"""
This module provides a function to divide all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number.
    
    Args:
        matrix (list of lists): A list of lists of integers or floats.
        div (int/float): The divisor.

    Returns:
        list of lists: A new matrix with all elements divided by div, rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats,
                   if rows are not of the same size, or
                   if div is not a number.
        ZeroDivisionError: If div is zero.
    """
    # Validate matrix
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    if not all(isinstance(element, (int, float)) for row in matrix for element in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Validate div
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Perform division
    return [[round(element / div, 2) for element in row] for row in matrix]

