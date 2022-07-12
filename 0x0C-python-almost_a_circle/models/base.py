#!/usr/bin/python3
""" Module for Base class """


class Base:
    """A python class called Base"""

    __nb_objects = 0
    def __init__(self, id=None):
        """Function to initalize class"""
        if(id is not None):
            self.id = id
        else:
            __nb_objects += 1
            self.id = __nb_objects

