#!/usr/bin/python3
"""
Square class that inherits from Rectangle.
"""

from rectangle import Rectangle

class Square(Rectangle):
    """
    Represents a square, which is a special case of a rectangle.
    """
    def __init__(self, size, x=0, y=0):
        """
        Initialize a new Square instance.

        Args:
            size (int): The size of the square (both width and height).
            x (int): The x position of the square.
            y (int): The y position of the square.
            id (int): Optional id of the instance.
        """

        super().__init__(size, size, x, y, id)

        def __str__(self):
            """
            Return the string representation of the Square.

            Format:
                [Square] (<id>) <x>/<y> - <size>
            """
            return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
