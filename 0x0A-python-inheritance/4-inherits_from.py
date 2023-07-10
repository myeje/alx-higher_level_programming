#!/usr/bin/python3
"""Python function"""


def inherits_from(obj, a_class):
    """
    inherits_from - function that checks if an object is
    an instance of or is an instance of a class that inherited from
    @obj: list object
    @a_class: check with
    Return: True or false
    """
    return (issubclass(type(obj), a_class) and type(obj) is not a_class)
