#!/usr/bin/python3
"""Python function"""


def is_kind_of_class(obj, a_class):
    """
    is_kind_of_class - function that checks if an object is
    an instance of or is an instance of a class inherited from
    @obj: list object
    @a_class: check with
    Return: True or false
    """
    return (isinstance(obj, a_class))
