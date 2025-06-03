#!/usr/bin/python3
"""Module for appending text to a UTF-8 file."""
 

def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF8).

    Args:
        filename (str): The name of the file to append to.
        text (str): The string to be appended.

    Returns:
        int: The number of characters added.
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
