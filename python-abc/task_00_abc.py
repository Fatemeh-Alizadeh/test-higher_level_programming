#!/usr/bin/env python3
from abc import ABC, abstractmethod

class Animal(ABC):
    """
    Abstract base class representing an Animal.
    """

    @abstractmethod
    def sound(self):
        """
        Abstract method that should be implemented by all subclasses
        to return the sound the animal makes.
        """
        pass

class Dog(Animal):
    """
    Dog class that inherits from Animal and implements the sound method.
    """
    def sound(self):
        return "Bark"

class Cat(Animal):
    """
    Cat class that inherits from Animal and implements the sound method.
    """
    def sound(self):
        return "Meow"
