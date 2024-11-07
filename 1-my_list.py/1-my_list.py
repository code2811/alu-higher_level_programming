#!/usr/bin/python3
"""Define a class MyList that inherits from list."""

class MyList(list):
    """Implement sorted printing for the list."""

    def print_sorted(self):
        """Print the list, but sorted in ascending order."""
        print(sorted(self))
