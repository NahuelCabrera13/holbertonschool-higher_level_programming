#!/usr/bin/python3
"""pepe"""


class BaseGeometry:
    """pepe"""
    def area(self):
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("<name> must be greater that 0")
        if value <= 0:
            raise ValueError("<name> must be greater that 0")
