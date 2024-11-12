#!/usr/bin/python3
"""
This module defines a function to read and print the contents of a file.
"""


def read_file(filename=""):
    """
    Reads the contents of a file and prints it to stdout.

    Args:
        filename (str): The name of the file to be read. Defaults to an empty string.

    Raises:
        None: The function does not raise any exceptions.
    """
    try:
        with open(filename, "r", encoding="UTF-8") as file:
            print(file.read())
    except FileNotFoundError:
        pass
