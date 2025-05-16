#!/usr/bin/python3
"""
This module defines the text_indentation function.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after '.', '?' and ':' characters.

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        if text[i] in ".?:":
            print(text[:i + 1].strip())
            print()
            text = text[i + 1:].lstrip()
            i = 0
        else:
            i += 1
    if text:
        print(text.strip(), end="")
