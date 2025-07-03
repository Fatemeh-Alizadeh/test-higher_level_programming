#!/usr/bin/python3
"""
This module prints a string with firstname and lastname
"""


def say_my_name(first_name, last_name=""):
    """
    This function prints a string with firstname and lastname
    Args:
    first_name (str)
    last_name (str)
    Return:
        a string with firstname and lastname
    Raises:
        TypeError: if first_name or last_name are not a string

    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    return print(f"My name is {first_name} {last_name}")
