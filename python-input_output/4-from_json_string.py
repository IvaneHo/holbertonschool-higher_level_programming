#!/usr/bin/python3
"""Module that converts a JSON string into a Python object."""
import json


def from_json_string(my_str):
    """
    Converts a JSON string into a corresponding Python object.

    Args:
        my_str (str): The JSON string to decode.

    Returns:
        object: The Python object represented by the JSON string.
    """
    return json.loads(my_str)
