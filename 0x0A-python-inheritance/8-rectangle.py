#!/usr/bin/python3
"""Rectangle class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class rectangle with inherited clas BaseGeometry"""
    def __init__(self, width, height):
        """
        Function initializes a rectangle class
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
