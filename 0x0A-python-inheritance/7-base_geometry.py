#!/usr/bin/python3
"""Class and function"""


class BaseGeometry():
    """
    empty class
    """
    def area(self):
        """function that raises exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Function that validates value"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
