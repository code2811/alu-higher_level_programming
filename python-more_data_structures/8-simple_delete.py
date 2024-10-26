#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """
    Deletes a key in a dictionary
    Args:
        a_dictionary: input dictionary
        key: key to delete (always a string)
    Returns:
        modified dictionary
    """
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
