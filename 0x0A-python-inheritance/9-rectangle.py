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

    def area(self):
        """
        Function that calculates the area of rectangle
        """
        return (self.__width * self.__height)

    def __str__(self):
        return ("[" + str(self.__class__.__name__) + "] " + str(self.__width)
                + "/" + str(self.__height))
