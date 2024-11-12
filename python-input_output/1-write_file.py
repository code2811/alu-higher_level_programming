#!/usr/bin/python3
"""
This module defines a function to write a string to a text file.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file and returns the number of characters written.

    Args:
        filename (str): The name of the file to write to. Defaults to an empty string.
        text (str): The string to be written to the file. Defaults to an empty string.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, "w", encoding="UTF-8") as file:
        num_chars_written = file.write(text)
        return num_chars_written