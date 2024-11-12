#!/usr/bin/python3
"""
This module defines a function to convert an object to its JSON representation.
"""
import json


def to_json_string(my_obj):
    """
    Convert an object to its JSON representation as a string.

    Args:
        my_obj (object): The object to be converted to JSON.

    Returns:
        str: The JSON representation of the object.
    """
    return json.dumps(my_obj)
