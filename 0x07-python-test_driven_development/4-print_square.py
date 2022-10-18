#!/usr/bin/python3
"""
This module consists of a function to print a square

Created on Tue Oct 18 2022
@author: Maurice Haro
"""


def print_square(size):
    """
    prints a square of given size using the # character

    Args:
        size (int): The size of the square

    Raises:
        TypeError: Exception if size is not an integer
        ValueError: Exception if size is less than 0
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif size == 0:
        print()
    else:
        for i in range(size):
            print('#' * size)

