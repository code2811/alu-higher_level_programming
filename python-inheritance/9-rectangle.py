#!/usr/bin/python3
# Import the BaseGeometry class from the 7-base_geometry module
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        # Validate and initialize width
        self.integer_validator("width", width)
        self.__width = width
        
        # Validate and initialize height
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        # Calculate and return the area of the rectangle
        return self.__width * self.__height

    def __str__(self):
        # Return the string representation of the rectangle
        return f"[Rectangle] {self.__width}/{self.__height}"

