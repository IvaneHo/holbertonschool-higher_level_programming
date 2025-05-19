#!/usr/bin/python3
"""Defines a class Square with size validation and area computation."""


class Square:
    """Represents a square with size and area methods."""

    def __init__(self, size=0):
        """Initializes the square with an optional size.

        Args:
            size (int): Size of the square (must be >= 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size < 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2
