#!/usr/bin/env python3
import math
from abc import ABC, abstractmethod

class Shape(ABC):
    """
    Abstract base class representing a geometric shape.
    """
    @abstractmethod
    def area(self):
        """
        Compute the area of the shape.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Compute the perimeter of the shape.
        """
        pass

class Circle(Shape):
    """
    Circle shape with a given radius.
    """
    def __init__(self, radius):
        """
        Initialise radius.
        """
        self.radius = radius

    def area(self):
        """
        Compute the area of the shape.
        """
        return math.pi * self.radius ** 2

    def perimeter(self):
        """
        Compute the perimeter of the shape.
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Rectangle shape with given width and height.
    """
    def __init__(self, width, height):
        """
        initialise width and height.
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Compute the area of the shape.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Compute the perimeter of the shape.
        """
        return 2 * (self.width + self.height)

def shape_info(shape):
    """
    Print the area and perimeter of any object that follows the Shape interface.
    """
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())
