#!/usr/bin/python3
"""Square class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class square with inherited clas BaseGeometry"""
    def __init__(self, size):
        """
        Function initializes a square class
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
