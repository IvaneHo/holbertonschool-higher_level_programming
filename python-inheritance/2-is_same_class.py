#!/usr/bin/python3
"""This module checks if an object is exactly an instance of a given class."""

def is_same_class(obj, a_class):
    """Check if obj is exactly an instance of a_class."""
    return type(obj) is a_class
