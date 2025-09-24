#!/usr/bin/python3
"""pepe"""


class BaseGeometry:
    """pepe"""
    def area(self):
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError("{} must be greater that 0".format(name))
        if value <= 0:
            raise ValueError("{} must be greater that 0".format(name))
