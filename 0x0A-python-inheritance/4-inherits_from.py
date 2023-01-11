#!/usr/bin/python3
"""
Module 4-inherits_from
Function thaat returns True/False
if the object is an instance of a class
"""


def inherits_from(obj, a_class):
    """
    Args:
        obj: object
        a_class: class type
    Returns: 
        True, if the object is an instance oc a class
        false, if otherwiswe
    """
    if issubclass(obj, a_class) and (type(obj) != a_class):
        return True
    return False


