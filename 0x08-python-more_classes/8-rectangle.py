#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This module contains a rectangle class with attributes
Created on Mon Oct 17 2022
@author: Maurice Haro
"""


class Rectangle:
    """
    Class Rectangle defining a simple rectangle

    Attributes:
        height: the heigth of the rectangle
        width: the width of the rectangle
        number_of_instances: The number of instances created
        print_symbol: Used as print symbol for string representation
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        The init method to initialise the instance varables

        Attributes:
            width (int, optional): The width of the rectangle
            height (int, optional): The height of the rectngle
            self.width = width
            self.height = height
            rectangle.number_of_instances += 1
        """
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def height(self):
        """
        Gets the property height

        Returns:
            height (int): the height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height property of the rectangle

        Attributes:
            value (int): The height of the rectangle

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        """
        Gets the property width

        Returns:
            width (int): the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width property of the rectangle

        Attributes:
            value (int): The width of the rectangle

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    def area(self):
        """
        Calculates the area of the rectangle

        Returns:
            The area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle

        Returns:
            The perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Prints the rectangle using character specified by cls attr print_symbol

        Returns:
            rect: The string representation of the rectangle with # character
        """

        rect = ""
        if self.__width == 0 or self.__height == 0:
            return rect

        for i in range(self.__height):
            for j in range(self.__width):
                rect += str(self.print_symbol)
            if i < self.__height - 1:
                rect += '\n'
        return rect

    def __repr__(self):
        """
        Adding a __repr__ method for the object rectangle

        Returns:
            rect (str): String representation of the rectangle
        """
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """
        Prints a message when the instance is deleted
        """

        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Determines biggest between two rectangles

        Args:
            rect_1: Rectangle 1
            rect_2: Rectangle 2

        Raises:
            TypeError: If any of args passed is not an instance of Rectangle

        Returns:
            The biggest rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        else:
            if rect_1.area() >= rect_2.area():
                return rect_1
            else:
                return rect_2

