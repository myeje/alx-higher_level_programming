#!/usr/bin/python3
"""Python function"""


def append_after(filename="", search_string="", new_string=""):
    """
    Function inserts a line of text to a file
    after each line containing a specific string
    """
    with open(filename, 'r+') as myFile:
        line = myFile.readlines()
        myFile.seek(0)

        for point in line:
            myFile.write(point)
            if search_string in point:
                myFile.write(new_string)
