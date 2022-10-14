#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 2022
@author: Maurice Haro
"""


class Square:
    """Modelling a square class with attiributes and instantiation with size

    Attributes:
        size (int): The size of the square
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialising instance attributes

        Args:
            size: (:obj: 'int', optional): A public instance size
            position: (:obj: 'tuple', optional): A public instance position
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Gets the property size
        Returns:
            The size of the square
        """
        return self.__size

    @property
    def position(self):
        """Gets the property position
        Returns:
            The tuples position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets position attribute and checks for errors

        Args:
            value: Value to chekc for errors

        Raises:
            TypeError: Exceptionif size is not an integer
        """
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) is not int or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    @size.setter
    def size(self, value):
        """
        Sets the size property and checks for errors

        Args:
            value: Value to check for errors

        Raises:
            TypeError: Exception if size is not an integer
            ValueError: Exception if size is less than 0
        """
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Calculates the area of the square

        Returns:
            Area of the square
        """
        return (self.__size**2)

    def my_print(self):
        """
        Print a square using # character
        """
        if (self.__size == 0):
            print()
        else:
            for i in range(self.position[1]):
                print()
            for i in range(self.size):
                for j in range(self.position[0]):
                    print(end=" ")
                for k in range(self.size):
                    print("#", end="")
                print()
