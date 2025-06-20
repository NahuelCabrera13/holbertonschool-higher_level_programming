#!/usr/bin/env python3
"""pepe"""

import pickle


class CustomObject:
    """pepe"""

    def __init__(self, name, age, is_student):
        
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
       
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")


    def serialize(self, filename):
  
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception:
            return None


    @classmethod
    def deserialize(cls, filename):
      
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except (FileNotFoundError, pickle.PickleError, EOFError):
            return None