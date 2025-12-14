#!/usr/bin/python3
"""
This module demonstrates abstract base classes and duck typing in Python.
It defines an abstract Shape class and concrete Circle and
Rectangle implementations.
"""

import math
from abc import ABC, abstractmethod


class Shape(ABC):
    """
    Abstract base class for shapes.
    Defines the interface that all shapes must implement.
    """
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """
    Class representing a circle.
    Inherits from the Shape abstract class and implements the area
    and perimeter methods.
    """
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius) ** 2

    def perimeter(self):
        return 2 * math.pi * abs(self.radius)


class Rectangle(Shape):
    """
    Class representing a rectangle.
    Inherits from the Shape abstract class and implements
    the area and perimeter methods.
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):

        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(shape):
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")