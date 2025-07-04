#!/usr/bin/python3
"""
Returns the JSON representation of an object as a string.
"""


import json

def to_json_string(my_obj):
    """
    Returns the JSON representation of an object as a string.

    Args:
        my_obj: The object to serialize.

    Returns:
        str: The JSON string representation of the object.
    """
    return json.dump(my_obj)
