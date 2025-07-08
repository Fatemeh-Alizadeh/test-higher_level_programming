#!/usr/bin/python3
"""
Square class that inherits from Rectangle.
"""

from models.rectangle import Rectangle

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

if __name__ == "__main__":

    s1 = Square(5)
    print(s1)
    print(s1.area())
    s1.display()

    print("---")

    s2 = Square(2, 2)
    print(s2)
    print(s2.area())
    s2.display()

    print("---")

    s3 = Square(3, 1, 3)
    print(s3)
    print(s3.area())
    s3.display()