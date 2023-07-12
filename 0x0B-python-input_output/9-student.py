#!/usr/bin/python3
"""Python class"""


class Student():
    """class student"""
    def __init__(self, first_name, last_name, age):
        """Initialize"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        function that returns the dictionary description
        with simple data structures
        """
        return (self.__dict__)
