#!/usr/bin/python3
"""
Function that adds 2 integers
"""


def add_integer(a, b=98):
    """
    add_integer - module adds 2 integers
    @a: first integer argument
    @b: second integer argument
    Return: sum of arguments

    Raise errors:
    TypeError: if arguments are not integer or float
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
