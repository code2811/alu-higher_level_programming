#!/usr/bin/python3
"""Define a Square class that inherits from Rectangle."""
from rectangle import Rectangle

class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

    def __str__(self):
        """Return the print and string representation of a Square."""
        return "[Square] {}/{}".format(self.__size, self.__size)
