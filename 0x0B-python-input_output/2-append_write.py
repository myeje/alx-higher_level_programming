#!/usr/bin/python3
"""Python function"""


def append_write(filename="", text=""):
    """Function that appends a string to a text file"""
    with open(filename, mode="a", encoding="utf-8") as myFile:
        return (myFile.write(text))
