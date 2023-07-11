#!/usr/bin/python3
"""Python function"""


def read_file(filename=""):
    """Function that read a text file"""
    with open(filename, encoding="utf-8") as myFile:
        print(myFile.read(), end="")
