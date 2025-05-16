#!/usr/bin/python3
"""
This module provides a function that prints text with
2 new lines after '.', '?' and ':' characters.
"""


def text_indentation(text):
    """
    Prints text with 2 new lines after '.', '?' and ':'.

    Args:
        text (str): The input string.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    current = ""
    for char in text:
        current += char
        if char in ".?:":
            print(current.strip())
            print()
            current = ""
    if current.strip() != "":
        print(current.strip())
