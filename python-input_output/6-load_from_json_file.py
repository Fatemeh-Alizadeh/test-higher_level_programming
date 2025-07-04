#!/usr/bin/python3
"""
Creates a Python object from a JSON file.
"""
import json


def load_from_json_file(filename):
    """
    Creates a Python object from a JSON file.

    Args:
        filename (str): The path to the JSON file.

    Returns:
        object: The Python object represented by the JSON content of the file.
    """
    with open(filename, "r", encoding="utf_8") as f:
        return json.load(f)
