#!/usr/bin/python3
"""
Module containing a function that checks if an object is an instance of
a class that inherited (directly or indirectly) from the specified class.
"""

def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class. Otherwise, returns False.

    Args:
        obj (object): The object to check.
        a_class (type): The class to compare against.

    Returns:
        bool: True if the object is an instance of a class that inherited
        (directly or indirectly) from the specified class. False otherwise.
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
