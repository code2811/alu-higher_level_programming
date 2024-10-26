#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Create a new matrix with the same size using list comprehension
    return [[x ** 2 for x in row] for row in matrix]
