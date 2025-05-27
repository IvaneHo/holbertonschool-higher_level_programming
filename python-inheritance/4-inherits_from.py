#!/usr/bin/python3
"""Check if object inherits from a given class."""


def inherits_from(obj, a_class):
    """
    Return True if obj is an instance of a subclass of a_class,
    otherwise return False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
