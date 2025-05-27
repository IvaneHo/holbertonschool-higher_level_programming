#!/usr/bin/env python3
"""Shape abstract base with Circle and Rectangle for duck typing."""

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
        if radius <= 0:
            raise ValueError("radius must be positive")
        self.__radius = radius

    def area(self):
        return math.pi * self.__radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.__radius


class Rectangle(Shape):
    def __init__(self, width, height):
        if not isinstance(width, (int, float)):
            raise TypeError("width must be a number")
        if not isinstance(height, (int, float)):
            raise TypeError("height must be a number")
        if width <= 0 or height <= 0:
            raise ValueError("width and height must be positive")
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * (self.__width + self.__height)


def shape_info(shape):
    """Print area and perimeter of the given shape."""
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
