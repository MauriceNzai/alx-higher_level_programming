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

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
