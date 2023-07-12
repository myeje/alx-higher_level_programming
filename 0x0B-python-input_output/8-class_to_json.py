#!/usr/bin/python3
"""Python function"""


def class_to_json(obj):
    """
    function that returns the dictionary description 
    with simple data structures
    """
    return (obj.__dict__)
