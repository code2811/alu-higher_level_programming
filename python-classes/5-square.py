#!/usr/bin/python3
"""Defines a Square class with printing capabilities."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initializes a new Square instance.

        Args:
            size (int): The size of the new Square. Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """Retrieves the size of the square."""
        return self.__size
