#!/usr/bin/python3
"""
Module 0-lookup
We are tp write a
function that returns the list of available attributes and methods of an object
"""

def lookup(obj):
    """
    Args: 
        obj: It is an instance of the class
    Returns: 
        List of attributes
    """
    return dir(obj)

