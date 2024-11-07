#!/usr/bin/python3
"""Module for Square class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square"""

    def __init__(self, size):
        """Initializes a Square instance

        Args:
            size (int): The size of the square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Calculates the area of the square"""
        return self.__size ** 2

    def __str__(self):
        """Returns the square description"""
        return f"[Square] {self.__size}/{self.__size}"
