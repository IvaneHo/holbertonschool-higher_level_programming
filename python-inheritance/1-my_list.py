#!/usr/bin/python3
"""Defines a subclass of list with a sorted print method."""


class MyList(list):
    """Custom list that can print itself sorted."""

    def print_sorted(self):
        """Print the list sorted in ascending order."""
        print(sorted(self))
