#!/usr/bin/python3
"""Function that prints a square with character #"""


def print_square(size):
    """
    print_square - function that prints a square with char #
    @size: length of the square
    Return: size by size of char #

    raise error:
        TypeError: if size is not int or is float and less than 0
        ValueError: if size is less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if not isinstance(size, float) and size < 0:
        raise TypeError("size mus be an integer")
    for x in range(0, size):
        for y in range(size):
            print("#", end="")
        print("")
