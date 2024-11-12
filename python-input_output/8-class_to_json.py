#!/usr/bin/python3
"""Module for class_to_json method"""


def class_to_json(obj):
    """Returns dictionary description for JSON serialization of an object
    Args:
        obj: instance of a Class
    Returns:
        dict: dictionary description of object
    """
    return obj.__dict__
