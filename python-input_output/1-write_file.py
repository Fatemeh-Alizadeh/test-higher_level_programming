#!/usr/bin/python3
"""
Appends a string to the end of a UTF-8 text file
and returns the number of characters added.
"""


def write_file(filename="", text=""):
    """
    Appends a string to the end of a UTF-8 text file.

    Args:
        filename (str): The name of the file to write to.
        text (str): The text to append.

    Returns:
        int: The number of characters added to the file.
    """
    with open(filename, "a",  encoding="utf-8") as f:
        return f.write(text)
