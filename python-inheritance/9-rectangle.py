#!/usr/bin/python3
"""
This module defines a Rectangle class that inherits from BaseGeometry.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """
    Represents a rectangle with width and height validated as positive integers.

    Methods:
        __init__(self, width, height): Initializes the width and height of the rectangle.
        area(self): Returns the area of the rectangle.
        __str__(self): Returns a string representation of the rectangle in [Rectangle] <width>/<height> format.
    """

    def __init__(self, width, height):
        """
        Initializes a rectangle with the specified width and height.
        
        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        
        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is not a positive integer.
        """
        self.integer_validator("width", width)
        self.__width = width
        
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Calculates and returns the area of the rectangle.
        
        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a string representation of the rectangle in [Rectangle] <width>/<height> format.
        
        Returns:
            str: String representation of the rectangle.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"


