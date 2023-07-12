#!/usr/bin/python3
"""Python function"""
import json


def save_to_json_file(my_obj, filename):
    """Function that writes an obj to a text file using JSON repr"""
    with open(filename, "w") as myFile:
        json.dump(my_obj, myFile)
