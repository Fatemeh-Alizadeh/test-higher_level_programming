#!/usr/bin/python3
"""
Writes an object to a text file using its JSON representation.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using its JSON representation.

    Args:
        my_obj: The object to serialize and write.
        filename (str): The name of the file to write to.
    """
    with open(filename, "w", encoding="utf_8") as f:
        json.dumps(my_obj, f)
