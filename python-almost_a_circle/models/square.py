#!/usr/bin/python3
"""
Square class that inherits from Rectangle.
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Represents a square, which is a special case of a rectangle.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a new Square instance.

        Args:
            size (int): The size of the square (both width and height).
            x (int): The x position of the square.
            y (int): The y position of the square.
            id (int): Optional id of the instance.
        """

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):

        self.width = value
        self.height = value

    def __str__(self):
        """
        Return the string representation of the Square.

        Format:
            [Square] (<id>) <x>/<y> - <size>
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):

        attrs = ["id", "size", "x", "y"]

        if args and len(args) > 0:
            for i, arg in args:
                while i <= len(attrs):
                    setattr(self, attrs[i], arg)

        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
