#!/usr/bin/python3
"""
Base class for managing id attribute across all future classes.
"""


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
