#!/usr/bin/python3
"""Defines a class Square with property getter and setter."""


class Square:
    """Represents a square with size and area methods."""

    def __init__(self, size=0):
        """Initializes the square with an optional size."""
        self.size = size  # Trigger the setter for validation

    @property
    def size(self):
        """Getter for the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for the size with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2
