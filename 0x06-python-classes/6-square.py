#!/usr/bin/python3
"""
Define a square
Has a private instance attribute: size
"""


class Square:
    """
    Class Square
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        creating an instance of square
        Attributes:
        size: integer value of size of square
        position: tuple containing position of square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """This getter function is called
        when the value of size is retrieved
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

    @property
    def position(self):
        """This getter function is called
        when the value of position is retrieved
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Setter protects from putting bad data"""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")  
        if not isinstance(value[1], int) or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Instance area that returns the current square area
        """
        return int(self.__size) ** 2

    def my_print(self):
        """
        Prints out the square with # char
        Using position for spaces
        """
        if self.size == 0:
            print()
        else:
            for x in range(self.position[1]):
                print()
            for x in range(self.size):
                for y in range(self.position[0]):
                    print(" ")
                for z in range(self.size):
                    print("#", end="")
                print()
