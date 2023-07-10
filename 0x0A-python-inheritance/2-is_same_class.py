#!/usr/bin/python3
"""Python function"""


def is_same_class(obj, a_class):
    """
    is_same_class - function that returns True if the object is
    exactly an instance of the specified class
    @obj: list object
    @a_class: check with
    Return: True or False
    """
    return (type(obj) is a_class)
