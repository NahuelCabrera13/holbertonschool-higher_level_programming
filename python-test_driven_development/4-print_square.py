#!/usr/bin/python3
"""pepe"""


def print_square(size):
    """pepe"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
