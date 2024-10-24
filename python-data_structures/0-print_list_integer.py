#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """
    Print all integers of a list.
    Args:
        my_list: list of integers (default empty list)
    Raises:
        TypeError: if an element in the list is not an integer
    """
    for number in my_list:
        if not isinstance(number, int):
            raise TypeError("list contains non-integer elements")
        print("{:d}".format(number))
