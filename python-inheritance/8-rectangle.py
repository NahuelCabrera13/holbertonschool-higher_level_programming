#!/usr/bin/python3
"""pepe"""


class BaseGeometry:
    """pepe"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if isinstance(value, bool):
            raise TypeError("{} must be an integer".format(name))
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        
class Rectangle(BaseGeometry):
    """pepe"""
        
    def __init__(self, width, height):

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.width = width
        self.height = height
