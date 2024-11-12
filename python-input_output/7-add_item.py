#!/usr/bin/python3
"""
Script that adds all arguments to a Python list and saves them to a file
"""
import sys
from os import path
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

# Name of the JSON file
filename = "add_item.json"

# Initialize the list
my_list = []

# Load existing data if file exists
if path.exists(filename):
    my_list = load_from_json_file(filename)

# Add all arguments to the list
my_list.extend(sys.argv[1:])

# Save the updated list to the JSON file
save_to_json_file(my_list, filename)
