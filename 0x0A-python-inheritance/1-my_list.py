#!/usr/bin/python3
"""
Module 1-my_list
Class that inherits from list
"""


class Mylist(list):
    """ Class that inherits the attributes references of class list
    Args:
        list: class list
    """

    def print_sorted(self):
        """Print the lists in a sorted ascending manner"""

        cpy_list = self.copy()
        cpy_list.sort()
        print("{}".format(cpy_list))

        
