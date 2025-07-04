#!/usr/bin/env python3

class Fish:
    """
    Base class representing a fish.
    """
    def swim(self):
        """
        Print swimming behavior of a fish.
        """
        print("The fish is swimming")
    def habitat(self):
        """
        Print habitat of a fish.
        """
        print("The fish lives in water")

class Bird:
    """
    Base class representing a bird.
    """
    def fly(self):
        """
        Print flying behavior of a bird.
        """
        print("The bird is flying")
    def habitat(self):
        """
        Print habitat of a bird.
        """
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    A class representing a flying fish, which can both swim and fly.
    Inherits from both Fish and Bird.
    """
    def fly(self):
        """
        Override Bird's fly method.
        """
        print("The flying fish is soaring!")

    def swim(self):
        """
        Override swim method.
        """
        print("The flying fish is swimming!")

    def habitat(self):
        """
        Override habitat method.
        """
        print("The flying fish lives both in water and the sky!")
