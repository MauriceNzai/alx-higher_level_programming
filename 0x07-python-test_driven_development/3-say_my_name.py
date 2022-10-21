#!/usr/bin/python3
"""
This module consists of a function that prints the first and last names

Created on Tue Oct 18 2022
@author: Maurice Haro
"""


def say_my_name(first_name, last_name=""):
    """
    Prints the "My name is + first and last name

    Args:
        first_name (str): First string to print
        last_name (str): Second string to print

    Raises:
        TypeError: Exception is arguments not strings
    """
    if type(first_name) is not str:
        raise TypeError("first name must be a string")

    elif type(last_name) is not str:
        raise TypeError("last name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
