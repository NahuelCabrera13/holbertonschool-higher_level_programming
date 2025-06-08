#!/usr/bin/python3
"""pepe"""
import json


def save_to_json_file(my_obj, filename):
    with open(filename, "w", encoding="utf-8")as  pepe:
        return json.dump(my_obj, pepe)
