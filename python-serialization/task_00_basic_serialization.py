#!/usr/bin/python3
"""Basic module to save and load a dictionary as JSON."""

import json


def serialize_and_save_to_file(data, filename):
    """
    Writes a Python dictionary to a JSON file.

    - Overwrites the file if it already exists.
    - Saves using UTF-8 encoding.
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """
    Loads a JSON file and returns its content as a Python dictionary.
    """
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
