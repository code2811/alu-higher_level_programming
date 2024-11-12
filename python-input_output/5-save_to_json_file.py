#!/usr/bin/python3
"""
This module defines a function to save an object to a JSON file.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Save an object to a text file in JSON representation.

    Args:
        my_obj (object): The object to be saved.
        filename (str): The name of the file to save the object to.

    Returns:
        None
    """
    with open(filename, "w", encoding="UTF-8") as file:
        json.dump(my_obj, file)
