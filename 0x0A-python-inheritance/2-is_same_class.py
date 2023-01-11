#!/usr/bin/python3
"""
Module 2-is_same_class
function that returns True if the object is exactly
an instance of the specified class
otherwise false
"""


def is_same_class(obj, a_class):
    """
    Args:
        obj: object
        a_class: class type
    Returns:
        True: if type of obj is a_class
        False: if otherwise
    """
    return type(obj) is a_class
