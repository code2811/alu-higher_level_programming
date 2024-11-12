#!/usr/bin/python3
"""
This script adds all arguments to a Python list and saves them to a file.
"""
import sys
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

filename = "add_item.json"

try:
    item_list = load_from_json_file(filename)
except FileNotFoundError:
    item_list = []

item_list.extend(sys.argv[1:])
save_to_json_file(item_list, filename)
