#!/usr/bin/python3
"""
This module defines the text_indentation function.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after '.', '?', and ':'.

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    start = 0
    for i, c in enumerate(text):
        if c in ".?:":
            print(text[start:i + 1].strip())
            print()
            start = i + 1
    if start < len(text):
        print(text[start:].strip(), end="")
