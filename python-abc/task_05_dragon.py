#!/usr/bin/env python3


class SwimMixin:
    """
    Mixin class providing swimming ability.
    """
    def swim(self):
        print("The creature swims!")

class FlyMixin:
    """
    Mixin class providing flying ability.
    """

    def fly(self):
        print("The creature flies!")

class Dragon(SwimMixin, FlyMixin):
    """
    Dragon class that can both swim and fly by inheriting from mixins.
    """
    def roar(self):
        print("The dragon roars!")

dragon = Dragon()
dragon.swim()
dragon.fly()
dragon.roar()
