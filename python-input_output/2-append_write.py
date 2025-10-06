#!/usr/bin/python3
"""pepe"""


def append_write(filename="", text=""):
    """pepe """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
