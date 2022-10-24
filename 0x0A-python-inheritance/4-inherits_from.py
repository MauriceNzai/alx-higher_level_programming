#!/usr/bin/python3
"""
Checks if object is subclass of a class
"""


def inherits_from(obj, a_class):
    """
    Returns true if its a subclass or false if not an instance
    """
    if type(obj) == a_class:
        return False
    return issubclass(type(obj), a_class)
