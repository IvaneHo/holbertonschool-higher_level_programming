#!/usr/bin/python3
"""Custom shapes using duck typing and abstract classes."""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Base class for geometric shapes."""

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """Circle defined by its radius."""
    def __init__(self, radius):
        if type(radius) not in (int, float):
            raise TypeError("radius must be a number")
        if radius <= 0:
            raise ValueError("radius must be positive")
        self.__r = radius

    def area(self):
        return math.pi * self.__r ** 2

    def perimeter(self):
        return 2 * math.pi * self.__r


class Rectangle(Shape):
    """Rectangle with width and height."""
    def __init__(self, width, height):
        for val, label in ((width, "width"), (height, "height")):
            if type(val) not in (int, float):
                raise TypeError(f"{label} must be a number")
            if val <= 0:
                raise ValueError(f"{label} must be positive")
        self.__w = width
        self.__h = height

    def area(self):
        return self.__w * self.__h

    def perimeter(self):
        return 2 * (self.__w + self.__h)


def shape_info(shape):
    """Displays area and perimeter of a shape-like object."""
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
