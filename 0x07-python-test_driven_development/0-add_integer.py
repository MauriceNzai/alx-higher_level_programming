#!/usr/bin/python3
"""
This module consists of a function that adds two integers

Created on Tue Oct 18 2022
@author Maurice Haro
"""

def add_integer(a, b=98):
    """
    Adds two integers

    Args:
        a: The first integer
        b: The second integer

    Returns:
        result: The result of addition a + b

    Raises:
        TypeError: If a or b is not an integer or a float value
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        result = int(a) + int(b)

    return result
