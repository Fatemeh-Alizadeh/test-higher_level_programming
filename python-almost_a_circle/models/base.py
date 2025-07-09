#!/usr/bin/python3
"""
Base class for managing id attribute across all future classes.
"""
import json
import os


class Base:
    """Base class for managing id attribute across all future classes."""

    __nb_objects = 0

    def __init__(self, id=None):

        """Initialize the Base instance with an id.

        Args:
            id (int, optional): The id to assign to the instance. If None,
                                an auto-incremented value is assigned.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Convert the list of dictionaries to a JSON string."""
        if list_dictionaries is None or []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save a list of objects to a JSON string."""

        filename = f"{cls.__name__}.json"
        if list_objs is None or []:
            dict_list = []
        else:
            dict_list = [obj.to_dictionary() for obj in list_objs]

        json_string = cls.to_json_string(dict_list)
        with open(filename, 'w') as f:
            return f.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """Parse a JSON string into a Python object."""
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create a new instance with a dictionary."""

        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = None

        if dummy:
            dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Load a JSON string into a Python object."""
        filename = f"{cls.__name__}.json"
        if not os.path.exists(filename):
            return []
        else:
            with open(filename, 'r', encoding='utf-8') as f:
                json_str = f.read()
                list_dicts = cls.from_json_string(json_str)
                return [cls.create(**d) for d in list_dicts]


