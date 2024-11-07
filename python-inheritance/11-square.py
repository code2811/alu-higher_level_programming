#!/usr/bin/python3
"""
This module contains the Square class that inherits from Rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle
    """
    def __init__(self, size):
        """
        Initialize a Square instance
        Args:
            size (int): size of the square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Calculate the area of the square
        Returns:
            int: area of the square
        """
        return self.__size ** 2

    def __str__(self):
        """
        Return string representation of the square
        Returns:
            str: description of the square
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
