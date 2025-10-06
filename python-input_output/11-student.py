#!/usr/bin/python3
"""pepe
"""


class Student:
    """pepe
    """

    def __init__(self, first_name, last_name, age):

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
   
        if attrs is None or not isinstance(attrs, list):
            return self.__dict__

        filtered_dict = {}
        for attr in attrs:
            if isinstance(attr, str) and hasattr(self, attr):
                filtered_dict[attr] = getattr(self, attr)

        return filtered_dict

    def reload_from_json(self, json):
    
        for key, value in json.items():
            setattr(self, key, value)