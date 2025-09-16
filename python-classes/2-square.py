#!/usr/bin/python3
"""pepe"""


class Square:
    """pepe"""

    def __init__(self, size=0):
        if isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
