#!/usr/bin/python3

class Square:

    """
    Modelling a square class with private attribute size
    and instantiation with optional size
    """
    def __init__(self, size=0):
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size
        """
        initializes instance attributes of a square
        Args:
            __size(int): size of square
            __position(tuple):position
        """

    def area(self):
        return (self.__size**2)

    """
    Returns the area of square based on size attribute
    """
