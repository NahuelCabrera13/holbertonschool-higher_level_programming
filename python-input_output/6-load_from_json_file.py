#!/usr/bin/python3
"""pepe
"""
import json


def load_from_json_file(filename):
    """pepe
    """
    with open(filename, 'r') as f:
        return json.load(f)
