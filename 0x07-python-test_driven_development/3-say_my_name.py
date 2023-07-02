#!/usr/bin/python3
""""Function that prints a string with format"""


def say_my_name(first_name, last_name=""):
    """
    say_my_name - module that prints a string with format
    @first_name: first argument string
    @last_name: second argument string
    Return: String with format of the two arguments

    raise errors:
        TypeError: if arguments are not string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
