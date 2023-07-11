#!/usr/bin/python3
"""Python function"""


def write_file(filename="", text=""):
    """Function that writes a string to a text file"""
    with open(filename, mode="w", encoding="utf-8") as myFile:
        return (myFile.write(text))
