#!/usr/binpyhton3
"""
lookup
"""
def lookup(obj):
    """
    Returns a list of available attributes and methods of an object
    """
    return ([item for item in dir(obj)])
