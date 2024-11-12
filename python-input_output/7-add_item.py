#!/usr/bin/python3
"""
This script adds all arguments to a Python list and saves them to a file named "add_item.json".
"""
import sys
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file


def main():
    """
    The main function that adds arguments to a list and saves it to a file.
    """
    filename = "add_item.json"

    try:
        item_list = load_from_json_file(filename)
    except FileNotFoundError:
        item_list = []

    item_list.extend(sys.argv[1:])
    save_to_json_file(item_list, filename)


if __name__ == "__main__":
    main()
