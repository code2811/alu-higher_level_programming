def square_matrix_simple(matrix=[]):
    """
    Computes the square value of all integers in a matrix
    Args:
        matrix: 2 dimensional array of integers
    Returns:
        A new matrix with each value being the square of the input value
    """
    if not matrix:
        return []
        
    return [[x ** 2 for x in row] for row in matrix]
