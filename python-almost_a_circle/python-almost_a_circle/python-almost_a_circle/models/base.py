#!/usr/bin/python3
"""Module for Base class"""

class Base:
    """Base class for managing id attribute"""
    
    # Private class attribute to track number of objects
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor for Base class
        
        Args:
            id (int, optional): Identifier for the instance
        """
        # Check if id is provided
        if id is not None:
            # If id is given, assign it directly
            self.id = id
        else:
            # If no id, increment the class counter and assign new id
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
