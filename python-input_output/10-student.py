#!/usr/bin/python3
"""Module that defines the Student class with optional attribute filtering."""


class Student:
    """Defines a student with first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initializes the Student with provided attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns a dict representation of the instance.
        If attrs is a list of strings, only return those attributes.
        """
        if isinstance(attrs, list) and all(isinstance(i, str) for i in attrs):
            return {key: getattr(self, key)
                    for key in attrs if hasattr(self, key)}
        return self.__dict__
