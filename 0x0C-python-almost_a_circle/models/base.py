#!/usr/bin/python3
"""Class Base"""


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Class Constructor"""
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
