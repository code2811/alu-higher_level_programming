#!/usr/bin/python3
"""
Module for Square class that inherits from Rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class representing a square, inheriting from Rectangle.
    This class defines a square by its size and implements
    area calculation with custom string representation.
    """

    def __init__(self, size):
        """
        Initialize a Square instance.

        Args:
            size (int): The size of the square sides
        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than or equal to 0
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
            int: The area of the square
        """
        return self.__size ** 2

    def __str__(self):
        """
        Return string representation of the square.

        Returns:
            str: Description of the square in format [Square] <width>/<height>
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
