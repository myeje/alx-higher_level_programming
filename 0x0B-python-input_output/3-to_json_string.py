#!/usr/bin/python3
"""Python module"""
import json


def to_json_string(my_obj):
    """Function that returns the JSON repr of an object"""
    return json.dumps(my_obj)
