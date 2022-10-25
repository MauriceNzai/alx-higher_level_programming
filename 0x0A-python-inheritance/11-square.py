#!/usr/bin/python3
"""
square class
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    creates class square
    inherits Rectangle class
    """

    def __init__(self, size):
        """
        initializing instance attributes
        """

        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        """
        Returns string representation of the square
        """
        return '[Square] {}/{}'.format(self.__size, self.__size)
