#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 2022
@author: Maurice Haro
"""


class Square:
    """
    Modelling a square class with private attribute size
    and instatiation with optional size
    """

    def __init__(self, size=0):
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size
        """
        initializes instance of a square
        Args:
            __size(int): size of square
            size must be positive and integer type
        """
