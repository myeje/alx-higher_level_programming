#!/usr/bin/python3
"""
Define a square
Has a private instance attribute: size
"""


class Square:
    """
    Class Square
    """

    def __init__(self, size=0):
        """
        creating an instance of square that represents its size
        Raises TypeError if instance is not an integer
        or ValueError if instance is less than 0
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        """This getter function is called
        when the value of height is retrieved
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter protects from putting bad data"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Instance area that returns the current square area
        """
        return int(self.__size) ** 2

    def my_print(self):
        """Prints out the square with # char"""
        if self.__size == 0:
            print()
        else:
            for x in range(self.__size):
                for y in range(self.__size):
                    print("#", end="")
                print()
