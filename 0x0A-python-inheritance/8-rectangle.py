#!/usr/bin/python3
"""
basegeomentryclass
"""


class BaseGeometry:
    """
    instance of geometry class
    """
    def __init__(self):
        """
        initializing instance
        """
    def area(self):
        """
        raise exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validates if value is integer
                        is positive
        """

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


"""
class rectangle
inherits class basegeometry
"""

class Rectangle(BaseGeometry):
    """
    creates a rectangle class
    initialized with width and height
    """
    def __init__(self,width, height):
        """
        initializing instance attributes
        """
        if not super().integer_validator("width", width):
            self.__width = width
        if not super().integer_validator("height", height):
            self.__height = height
