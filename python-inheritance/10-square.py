#!/usr/bin/python3
"""Rectangle class"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """pepe"""

    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

     def area(self):
        return self.__width * self.__height

    def __str__(self):
        return "[Square] {}/{}" .format(self.__width, self.__height)

