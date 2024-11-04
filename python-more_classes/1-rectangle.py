#!/usr/bin/python3
"""
This module defines a Rectangle class with width and height properties.
"""


class Rectangle:
    """Defines a rectangle with width and height properties."""

    def __init__(self, width=0, height=0):
        """Initialize the rectangle with optional width and height."""
        self.width = width
        self.height = height


    def width(self):
        """Retrieve the width of the rectangle."""
        return self.__width


    def width(self, value):
        """Set the width of the rectangle, with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value


    def height(self):
        """Retrieve the height of the rectangle."""
        return self.__height

    
    def height(self, value):
        """Set the height of the rectangle, with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

