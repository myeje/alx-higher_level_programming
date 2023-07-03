#!/usr/bin/python3
"""Creating a class rectangle"""


class Rectangle:
    """Class rectangle"""
    number_of_instances = 0
    print_symbol = "#"

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
        Rectangle.number_of_instances += 1

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

    def area(self):
        """area of rectangle"""
        return (int(self.__width) * int(self.__height))

    def perimeter(self):
        """Perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return (int(self.__width) * 2) + (int(self.__height) * 2)

    def __str__(self):
        """printing the rectangle with character #"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        rect = ""
        for both in range(self.__height):
            rect += str(self.print_symbol) * self.__width
            if both < self.__height - 1:
                rect += "\n"
        return (rect)

    def __repr__(self):
        """"Prints out the string representation of the rectangle"""
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """
        Print out message when an instance of rectangle
        is about to be deleted
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Static method to get bigger rectangle"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        else:
            return (rect_2)

    @classmethod
    def square(cls, size=0):
        """class method to replace vlaue of width and height with size"""
        return (Rectangle(size, size))
