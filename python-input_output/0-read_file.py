#!/usr/bin/python3
"""
Reads a UTF-8 encoded text file and prints its contents to stdout.
"""


def read_file(filename=""):
    """
    Reads a UTF-8 encoded text file and prints its contents to stdout.

    Args:
        filename (str): The name of the file to read. Defaults to an empty string.
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
