#!/usr/bin/python3
"""Add all arguments to a Python list and save them to a file."""
import sys
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

# Name of the file to store the list
filename = "add_item.json"

# Try to load existing items from file, create empty list if file doesn't exist
try:
    items = load_from_json_file(filename)
except FileNotFoundError:
    items = []

# Add all arguments to the list
items.extend(sys.argv[1:])

# Save the updated list to the file
save_to_json_file(items, filename)
