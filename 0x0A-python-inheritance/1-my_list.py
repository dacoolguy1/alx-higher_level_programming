#!/usr/bin/python3
"""
Module 1-my_list
Function that returns the list of available attributes
and methods of an object
"""


class Mylist(list):
    """ Class that inherits the attributes references of class list
    Args:
        list: class list
    """

    def print_sorted(self):
        """Print the lists in a sorted ascending manner"""

        list_cpy = self.copy()
        list_cpy.sort()
        print("{}".format(list_cpy))
