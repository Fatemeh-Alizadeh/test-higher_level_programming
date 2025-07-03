#!/usr/bin/python3
"""
This is a  function that prints a text with 2 new lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
       Prints text with two new lines after each '.', '?' or ':' character.

       Args:
           text (str): The text to format and print.

       Raises:
           TypeError: If text is not a string.
       """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    start = 0
    for i in range(len(text)):
        if text[i] in ".?:":

            print(text[start:i + 1].strip())
            print()
            print()
            start = i + 1

    if start < len(text):
        print(text[start:].strip())
