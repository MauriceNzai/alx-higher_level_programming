#!/usr/bin/python3

"""
Class MyList
Module created on Mon 24 Oct 2022
@author: Maurice Haro

"""

class MyList(list):
    """
    inherits attributes of the list class

    """
    def print_sorted(self):
        """
        Prints the list sorted in ascending order

        """
        print(sorted(self))
