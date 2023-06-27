#!/usr/bin/python3
"""
Define a square
Has a private instance attribute: size
"""


class Square:
        """
        Class Square
        """
        def __init__(self, size=0):
            """
            creating an instance of square that represents its size
            Raises TypeError if instance is not an integer
            or ValueError if instance is less than 0
            """

            if not isinstance(size, int):
                raise TypeError("size must be an integer")
            elif size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
