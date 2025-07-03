#!/usr/bin/env python3

class VerboseList(list):
    """
    A custom list class that prints messages whenever items are added or removed.
    """
    def append(self, item):
        """
        Added [{item}] to the list.
        """
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, items):
        """
        Extended the list with [{count}] items.
        """
        super().extend(items)
        count = len(items)
        print(f"Extended the list with [{count}] items.")

    def remove(self, item):
        """
        Removed [{item}] from the list.
        """
        super().remove(item)
        print(f"Removed [{item}] from the list.")

    def pop(self, index=-1):
        """
        Popped [{self[index]}] from the list.
        """
        print(f"Popped [{self[index]}] from the list.")
        super().pop(index)
