#!/usr/bin/python3
"""Module that converts an object to a JSON string."""
import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object.

    Args:
        my_obj (any): The object to convert.

    Returns:
        str: The JSON string representation.
    """
    return json.dumps(my_obj)
