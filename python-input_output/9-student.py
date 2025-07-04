#!/usr/bin/python3
"""
Defines a student by first name, last name, and age.
"""


class Student:
    """
    Defines a student by first name, last name, and age.
    """
    def __init__(self, first_name, last_name, age):
        """
        Initialize a Student instance.

        Args:
            first_name
            last_name
            age (int):
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieve a dictionary representation of the Student instance.
        """
        return self.__dict__
