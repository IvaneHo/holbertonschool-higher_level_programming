#!/usr/bin/python3
"""
This module provides a function to add two integers.
It handles integer and float inputs.
If inputs are invalid, a TypeError is raised.
Float inputs are cast to integers.

Examples:
    >>> add_integer(1, 2)
    3
    >>> add_integer(100)
    198
    >>> add_integer(100.5, 1)
    101
    >>> add_integer(4, "School")
    Traceback (most recent call last):
        ...
    TypeError: b must be an integer
    >>> add_integer(None)
    Traceback (most recent call last):
        ...
    TypeError: a must be an integer
"""

def add_integer(a, b=98):
    """
    Adds two integers or floats casted to integers.

    Returns the result of a + b as an integer.

    Raises:
        TypeError: If a or b are not integers or floats.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
