#!/usr/bin/python3
"""Class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class that creates a square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor"""
        self.size = size
        self.x = x
        self.y = y
        self.id = None
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Retrieves the size"""
        return self.__width

    @size.setter
    def size(self, value):
        """Sets the size to value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value

    def __str__(self):
        """Returns a formated string"""
        return (f"[square] ({self.id}) {self.x}/{self.y} - {self.size}")

    def update(self, *args, **kwargs):
        """Function that assigns an argument to each attribute"""
        if len(args) != 0:
            attributes = ['id', 'size', 'x', 'y']
            for i, arg in enumerate(args):
                setattr(self, attributes[i], arg)
        elif len(kwargs) != 0:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        This function returns
        the dictionary representation of a rectangle
        """
        return ({'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y})
