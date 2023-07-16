#!/usr/bin/python3
"""Class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class that creates a square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor"""
        super().__init__(size, size, x, y, id)
        self.size = size
        self.x = x
        self.y = y

    @property
    def size(self):
        """Retrieves the size"""
        return self.__width

    @size.setter
    def size(self, value):
        """Sets the size to value"""
        self.__width = value
        self.__height = value

    def __str__(self):
        """Returns a formated string"""
        return (f"[square] ({self.id}) {self.x}/{self.y} - {self.size}")
