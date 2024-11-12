#!/usr/bin/python3
"""
This module defines a function to append a string to a text file.
"""


def append_write(filename="", text=""):
    """
    Appends a string to the end of a text file and returns the number of characters added.

    Args:
        filename (str): The name of the file to append to. Defaults to an empty string.
        text (str): The string to be appended to the file. Defaults to an empty string.

    Returns:
        int: The number of characters added to the file.
    """
    with open(filename, "a", encoding="UTF-8") as file:
        num_chars_added = file.write(text)
        return num_chars_added
