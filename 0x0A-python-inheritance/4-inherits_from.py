#!/usr/bin/python3
"""
Module 4-inherits_from
Function thaat returns True/False
if the object is an instance of a class
"""


def inherits_from(obj, a_class):
    """
    return True if object is an instance of a class that
    inherited from specified class
    """
    if issubclass(type(obj), a_class) and (type(obj) != a_class):
        return True
    return False
