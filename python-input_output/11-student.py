#!/usr/bin/python3
"""Module defining the Student class with JSON serialization and reloading."""


class Student:
    """A class to represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize the student with first name, last name, and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dict representation of the instance.
        If attrs is a list of strings, filter the attributes returned.
        """
        if isinstance(attrs, list) and all(type(a) is str for a in attrs):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Update attributes from a dictionary."""
        for key in json:
            setattr(self, key, json[key])
