#!/usr/bin/python3

def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean)
    for JSON serialization of an object.
    
    Args:
        obj (object): An instance of a Class.
    
    Returns:
        dict: A dictionary description of the object.
    """
    return {key: value for key, value in obj.__dict__.items() if isinstance(value, (list, dict, str, int, bool))}_
