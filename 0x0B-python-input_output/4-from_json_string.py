#!/usr/bin/python3
"""Python function"""
import json


def from_json_string(my_str):
    """Function that returns an object repr by a JSON string"""
    return json.loads(my_str)
