#!/usr/bin/python3
class Square:
    """
    Modelling a square class with instance attribute size
    """
    def __init__(self, size=0):
        self.__size = size
    """
    initializes a square size attributes
    Args:
        __size(int): size of square private property
    """
    @property
    def size(self):
        return self.__size
    """
    Property getter
    Gets size of square
    """
    @size.setter
    def size(self, value):
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value
        """
        Property setter
        sets size of square
        square must be integer and greater than 0
        """
    def area(self):
        return (self.__size**2)
        """
        Returns the area of square based on its size attribute
        """
