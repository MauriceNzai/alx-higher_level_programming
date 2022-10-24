#!/usr/binpyhton3
def lookup(obj):
    """
    Returns a list of available attributes and methods of an object

    Args:
        obj: The object whose attributes an methods are to be printed

    Returns: A list object

    """

    return ([item for item in dir(obj)])
