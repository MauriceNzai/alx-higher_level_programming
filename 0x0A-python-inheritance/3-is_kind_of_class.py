#!/usr/bin/python3
"""
Checks if an instance is an object of a class
"""


def is_kind_of_class(obj, a_class):
    """
    Returns true if its an instance or false if not an instance
    """
    return isinstance(obj, a_class)
