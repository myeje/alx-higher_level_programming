#!/usr/bin/python3
"""Python function"""


def lookup(obj):
    """
    lookup - Function that returns the list of available
    attributes and methods
    @obj: list object
    Return: list
    """
    return (dir(obj))
