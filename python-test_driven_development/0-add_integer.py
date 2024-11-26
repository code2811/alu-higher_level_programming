#!/usr/bin/python3
def add_integer(a, b=98):
    """
    Adds two integers after type checking and conversion.

    Args:
        a (int or float): First number to add.
        b (int or float, optional): Second number to add. Defaults to 98.

    Returns:
        int: The sum of a and b.

    Raises:
        TypeError: If a or b is not an integer or float.
    """
    # Check type of first argument
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    
    # Check type of second argument
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    # Cast to integers if they are floats
    a = int(a)
    b = int(b)
    
    # Return the sum
    return a + b
