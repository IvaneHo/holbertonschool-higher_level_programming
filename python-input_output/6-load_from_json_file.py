#!/usr/bin/python3
"""Module that loads a Python object from a JSON file."""
import json


def load_from_json_file(filename):
    """
    Loads and returns a Python object from a JSON file.

    Args:
        filename (str): The path to the file to read.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
