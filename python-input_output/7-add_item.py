#!/usr/bin/python3

import sys
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

def add_item():
    """
    Adds all command line arguments to a Python list and saves the list to a JSON file.
    """
    try:
        items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        items = []

    items.extend(sys.argv[1:])
    save_to_json_file(items, "add_item.json")

if __name__ == "__main__":
    add_item()

