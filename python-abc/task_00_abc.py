#!/usr/bin/env python3
"""Abstract class Animal and its subclasses Dog and Cat"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class for all animals"""

    @abstractmethod
    def sound(self):
        """Subclasses must implement this method"""
        pass


class Dog(Animal):
    """Dog subclass of Animal"""

    def sound(self):
        return "Bark"


class Cat(Animal):
    """Cat subclass of Animal"""

    def sound(self):
        return "Meow"
