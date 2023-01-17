#!/usr/bin/python3
"""
Module base.py
if id is not None, assign the public instance attribute
id with this argument value
otherwise, increment __nb_objects and assign the new value
to the public instance attribute id
"""
class Base:
    """
    Main class
    """
    __nb_objects = 0 
    """ a private atttribute hence it ca only be acceed inside this class"""
    def __init__(self, id=None):
        """ initializes objects attributes"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
