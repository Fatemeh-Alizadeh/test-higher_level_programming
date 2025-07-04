#!/usr/bin/env python3
"""
An iterator that wraps another iterable and keeps track of how many items
have been fetched using __next__.
"""


class CountedIterator:
    """
    An iterator that wraps another iterable.
    """

    def __init__(self, iterable):
        """
        initialise iterator and counter.
        """
        self.iterator = iter(iterable)
        self.counter = 0

    def __iter__(self):
        """
        Return the iterator object itself.
        """
        return self

    def __next__(self):
        """
        Return the next item from the underlying iterator and increment the count.
        """
        self.counter += 1
        return next(self.iterator)

    def get_count(self):
        """
        Returns the number of items that have been fetched so far.
        """
        return self.counter
