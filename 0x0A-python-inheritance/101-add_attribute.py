#!/usr/bin/python3
"""Python function"""


def add_attribute(obj, attribute, item):
    """
    Function that adds a new attribute to an object
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, item)
