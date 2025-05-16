#!/usr/bin/python3
"""
This module provides a function to add two integers.
It handles integer and float inputs.
If inputs are invalid, a TypeError is raised.
Float inputs are cast to integers.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats casted to integers.

    Returns:
        The sum of a and b as an integer.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
