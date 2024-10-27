def update_dictionary(a_dictionary, key, value):
    """
    Replaces or adds key/value pairs in a dictionary
    Args:
        a_dictionary: the input dictionary
        key: the key (always a string)
        value: the value to update or add (can be any type)
    Returns:
        The updated dictionary
    """
    a_dictionary[key] = value
    return a_dictionary
