#!/usr/bin/python3
"""
    The module is named "3-say_my_name".

    This module contains only one function named "say_my_name"
    and it only prints "My name is <first_name> <last_name>"
"""


def say_my_name(first_name, last_name=""):
    """This functions says the first name and last name"""
    if(type(first_name) is not str):
        raise TypeError("first_name must be a string")
    if(type(last_name) is not str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
