#!/usr/bin/python3
"""pepe"""
import json


def load_from_json_file(filename):
    """pepe"""
    with open(filename, "r", encoding="utf-8") as pepe:
        return json.load(pepe)
