#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 2022
@author: Maurice Haro
"""


class Square:
    """
    Modelling a square class with attributes and instatiates with size

    Attributes:
        size (int): The size of the square
    """

    def __init__(self, size):
        """
        initializes a square with parameters

        args:
            __size(int): size of the square
        """

        self.__size = size
