#!/usr/bin/python3
"""
Module 3-is_kind_of_class
function that returns True if the object is an instance
of, or if the object is an instance of a class 
that inherited from, the specified class 
otherwise False
"""


 def is_kind_of_class(obj, a_class):
     """
     Args:
        obj: object
        a_class: class type
    Returns:
        True: if the object is an instance of a class
        False: Otherwise
    """
    if isinstance(obj, a_class):
        return True
    return False
