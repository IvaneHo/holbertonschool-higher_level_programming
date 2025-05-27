#!/usr/bin/env python3
"""Abstract class Shape, with Circle and Rectangle subclasses using duck typing."""

from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """Abstract base class for geometric shapes."""

    @abstractmethod
    def area(self):
        """Must return area of shape"""
        pass

    @abstractmethod
    def perimeter(self):
        """Must return perimeter of shape"""
        pass


class Circle(Shape):
    """Circle shape, defined by its radius."""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2

    def perimeter(self):
        return 2 * pi * self.radius


class Rectangle(Shape):
    """Rectangle shape, defined by width and height."""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(obj):
    """Prints area and perimeter of any object with matching methods (duck typing)."""
    print("Area:", obj.area())
    print("Perimeter:", obj.perimeter())
