#!/usr/bin/python3
"""
This module defines a function to load an object from a JSON file.
"""
import json


def load_from_json_file(filename):
    """
    Load an object from a JSON file.

    Args:
        filename (str): The name of the file to load the object from.

    Returns:
        object: The Python object represented by the JSON file.
    """
    with open(filename, "r", encoding="UTF-8") as file:
        return json.load(file)
