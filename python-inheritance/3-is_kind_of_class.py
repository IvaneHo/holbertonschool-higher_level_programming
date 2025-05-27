#!/usr/bin/python3
"""Check if object is instance or inherits from a class."""


def is_kind_of_class(obj, a_class):
    """Return True if obj is an instance or inherits from a_class."""
    return isinstance(obj, a_class)
