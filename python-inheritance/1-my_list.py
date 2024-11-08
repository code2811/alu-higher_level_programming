#!/usr/bin/python3
"""This module defines the MyList class that inherits from list"""


class MyList(list):
    """A class that inherits from list and implements additional functionality

    This class extends the built-in list class and adds a method to print
    the list in sorted order.
    """

    def print_sorted(self):
        """Prints the list in ascending sorted order

        The original list remains unchanged.
        """
        print(sorted(self))
