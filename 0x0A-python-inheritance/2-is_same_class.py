#!/usr/bin/python3
"""
is_same_class
"""


def is_same_class(obj, a_class):
    """
    Returns True is the object is exactly an instance of the class;
    False otherwise
    """
    return type(obj) is a_class
