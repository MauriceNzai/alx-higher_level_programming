#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 2022
@author: Maurice Haro
"""


class Square:
    """
    Modelling a square class with instance attribute size
    """

    def __eq__(self, other):
        """
        Checks for equality of two squares
        """
        return self.__size == other.__size

    def __lt__(self, other):
        """
        Checks if is less than
        """
        return self.__size < other.__size

    def __le__(self, other):
        """
        Checks if less than or equal to
        """
        return self.__size <= other.__size

    def __ne__(self, other):
        """
        Checks if not equal to
        """
        return self.__size != other.__size

    def __gt__(self, other):
        """
        Checks if greater than
        """
        return self.__size > other.__size

    def __ge__(self, other):
        """
        Checks if greater than or equal to
        """
        return self.__size >= other.__size
    

    def __init__(self, size=0):
        """
        initializes a square size attributes
        Args:
            __size(int): size of square private property
        """
        self.__size = size

    @property
    def size(self):
        """
        Property getter
        Gets size of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        if (type(value) is not int):
            raise TypeError("size must be a number")

        if (type(value) is not float):
            raise TypeError("size must be a number")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value
       
    def area(self):
        return (self.__size ** 2)
        """
        Returns the area of square based on its size attribute
        """
