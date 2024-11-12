#!/usr/bin/python3
"""
Module for generating Pascal's Triangle
"""

def pascal_triangle(n):
    """
    Returns a list of lists of integers representing Pascal's triangle of n.
    
    Args:
        n (int): The number of rows to generate
        
    Returns:
        list: Empty list if n <= 0, otherwise list of lists representing triangle
    """
    if n <= 0:
        return []
        
    triangle = [[1]]  # Initialize with first row
    
    for i in range(1, n):
        # Start with 1
        row = [1]
        
        # Calculate middle numbers using previous row
        for j in range(1, i):
            prev_row = triangle[i-1]
            row.append(prev_row[j-1] + prev_row[j])
            
        # End with 1
        row.append(1)
        
        # Add row to triangle
        triangle.append(row)
        
    return triangle
