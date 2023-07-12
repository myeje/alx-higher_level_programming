#!/usr/bin/python3
"""Python function"""
import json


def load_from_json_file(filename):
    """Function that creates an object from a JSON file"""
    with open(filename) as myFile:
        json.load(myFile)
