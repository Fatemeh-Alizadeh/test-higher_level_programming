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

    def to_json(self, attrs=None):
        """
        Retrieve a dictionary representation of the Student instance.
        """
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            new_dic = {}
            for attr in attrs:
                if attr in self.__dict__:
                    new_dic[attr] = self.__dict__[attr]
            return new_dic

        else:
            return self.__dict__

    def reload_from_json(self, json):
        """
        Replace all attributes of the Student instance using a dictionary.
        """
        for key, value in json.items():
            self.__dict__[key] = value
