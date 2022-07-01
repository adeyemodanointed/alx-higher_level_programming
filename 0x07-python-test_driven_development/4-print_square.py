#!/usr/bin/python3
"""
    The module is named "4-print_square"

    It has only one function print_square
    which prints a square using "#"
"""


def print_square(size):
    """ Function print_square prints square using "#" """
    if(type(size) is not int):
        raise TypeError("size must be an integer")
    if(size < 0):
        raise ValueError("size must be >= 0")

    if(size == 0):
        print()
    else:
        for i in range(size):
            print("{}".format("#" * size))
