#!/usr/bin/python3
"""
Module 1-my_list
Function that return the list of available attributes
and methods of an object
"""


class MyList(list):
    """ Class that inherits the attributes references of class list
    Args:
        list: class list
    """

    def print_sorted(self):
        """ Method that prints the sorted list """

        cpy_list = self.copy()
        cpy_list.sort()
        print("{}".format(cpy_list))
