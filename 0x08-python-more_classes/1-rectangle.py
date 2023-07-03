#!/usr/bin/python3
"""Creating a class rectangle"""


class Rectangle:
    """Class rectangle"""
    def __init__(self, width=0, height=0):
        """
        object property for rectangle class
        @width: width of rectangle
        @height: height of rectangle

        Raise errors:
            TypeError: if arguments are not int
            ValueError: if arguments are in the negative
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """property getter to retrieve width"""
        return self.__width

    @width.setter
    def width(self, value):
        """property setter to set width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """property getter to retrieve height"""
        return self.__height

    @height.setter
    def height(self, value):
        """property setter to set height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
