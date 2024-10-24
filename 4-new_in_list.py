#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """Replace element at specific position in a copy of the list.

    Args:
        my_list: original list
        idx: index to replace element
        element: new element to insert

    Returns:
        Modified copy if index valid, copy of original list otherwise
    """
    list_copy = my_list[:]
    if idx < 0 or idx >= len(my_list):
        return list_copy
    list_copy[idx] = element
    return list_copy
