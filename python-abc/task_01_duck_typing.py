#!/usr/bin/env python3
"""Shape abstract base class with duck-typed Circle and Rectangle implementations."""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be a number")
        if isinstance(radius, bool) or radius <= 0:
            raise ValueError("radius must be a positive number")
        self.__radius = radius

    def area(self):
        return math.pi * self.__radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.__radius


class Rectangle(Shape):
    def __init__(self, width, height):
        if not all(isinstance(v, (int, float)) for v in (width, height)):
            raise TypeError("width and height must be numbers")
        if any(isinstance(v, bool) or v <= 0 for v in (width, height)):
            raise ValueError("width and height must be positive numbers")
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * (self.__width + self.__height)


def shape_info(shape):
    """Print area and perimeter of any duck-typed shape object."""
    if not (hasattr(shape, "area") and hasattr(shape, "perimeter")):
        raise TypeError("Object must have area and perimeter methods")
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
