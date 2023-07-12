#!/usr/bin/python3
"""Python class"""


class Student():
    """class student"""
    def __init__(self, first_name, last_name, age):
        """Initialize"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        function that retrievess the dictionary description
        with simple data structures
        """
        if attrs is None:
            return (self.__dict__)
        else:
            return {
                key: value
                for key, value in self.__dict__.items()
                if key in attrs
            }

    def reload_from_json(self, json):
        """
        Public method that replaces all attrs of the student instance
        """
        for k, v in json.items():
            setattr(self, k, v)
