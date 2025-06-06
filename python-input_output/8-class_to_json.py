#!/usr/bin/python3
"""Module that transforms a class instance into a serializable dictionary."""


def class_to_json(obj):
    """Returnsthedictionary description of an object for JSON serialization."""
    return obj.__dict__
