#!/usr/bin/python3
"""MyList class"""


class MyList(list):
    """Class MyList that inherits from list class"""
    def print_sorted(self):
        """Function that prints a sorted list"""
        print(sorted(self))
