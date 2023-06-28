#!/usr/bin/python3
import math
"""Magic class"""

class MagicClass:
    """Defining a magic class"""

    def __init__(self, radius=0):
        """initializing"""
        self.__radius = 0
        if not isinstance(radius, int) and not isinstance(radius, float):
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """gets the total surface area of the circle"""
        return ((self.__radius ** 2) * math.pi)

    def circumference(self):
        """Gets the circumference of the circle"""
        return (2 * math.pi * self.__radius)
