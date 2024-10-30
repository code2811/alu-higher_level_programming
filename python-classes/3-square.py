#!/usr/bin/python3
"""Defines a Square class with a private size attribute, size validation, and area calculation."""

class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initializes a new Square instance.

        Args:
            size (int): The size of the new Square. Defaults to 0.

        Raises:
            TypeError: If `size` is not an integer.
            ValueError: If `size` is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculates the current square area.

        Returns:
            int: The current square area.
        """
        return self.__size ** 2
