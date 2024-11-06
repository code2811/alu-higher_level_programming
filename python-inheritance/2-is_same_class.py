def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    Args:
        obj (object): The object to inspect.

    Returns:
        list: A list of strings containing the names of the available
        attributes and methods of the object.
    """
    return dir(obj)
