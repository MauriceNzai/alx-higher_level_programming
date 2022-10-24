#!/usr/bin/pyhton3
"""
lookup - check for attributes and methods
"""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object
    """
    return ([item for item in dir(obj)])
