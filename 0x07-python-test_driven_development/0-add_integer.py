#!/usr/bin/python3
"""
This is the "0-add_integer" module.

The 0-add_integer module supplies one function, add_integer(a, b).
"""


def add_integer(a, b=98):
    """Return the addition of two numbers."""
    if(type(a) != float and type(a) != int):
        raise TypeError("a must be an integer")
    if(type(b) != float and type(b) != int):
        raise TypeError("b must be an integer")
    return(int(a) + int(b))
