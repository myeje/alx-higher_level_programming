#!/usr/bin/python3
"""Rectangle class that creates a rectangle"""
from models.base import Base


class Rectangle(Base):
    """Class Rectangles"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Function that calculates the area of the rectangle"""
        return (self.__width * self.__height)

    def display(self):
        """Function that print the rectanglee instance with char '#'"""
        for _ in range(self.y):
            print()
        for row in range(self.height):
            for _ in range(self.x):
                print(" ", end="")
            for _ in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """function that returns a string"""
        return (f"[{self.__class__.__name__}]
                ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}")

    def update(self, *args, **kwargs):
        """Function that assigns an argument to each attribute"""
        if len(args) != 0:
            attributes = ['id', 'width', 'height', 'x', 'y']
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
        return ({'x': self.x, 'y': self.y, 'id': self.id,
                'height': self.height, 'width': self.width})
