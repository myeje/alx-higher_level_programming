#!/usr/bin/python3
"""MyInt class"""


class MyInt(int):
    """
    MyInt class that inherits int and inverts operations
    """
    def __eq__(self, integer):
        """"Inverts equality operator"""
        return (super().__ne__(integer))

    def __ne__(self, integer):
        """Inverts inequality operator"""
        return (super().__eq__(integer))
