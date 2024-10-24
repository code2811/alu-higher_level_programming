!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """Replace element at specific position in list.

    Args:
        my_list: input list
        idx: index to replace element
        element: new element to insert

    Returns:
        Modified list if index valid, original list otherwise
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return my_list


def print_reversed_list_integer(my_list=[]):
    """Print all integers of a list in reverse order.

    Args:
        my_list: input list (default empty list)
    """
    if my_list:
        for number in reversed(my_list):
            print("{:d}".format(number))
