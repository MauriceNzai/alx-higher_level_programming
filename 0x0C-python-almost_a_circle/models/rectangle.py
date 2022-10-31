#!/usr/bin/python3
"""
rectangle class: inherits base class

Created on Thur Oct, 27 2022

@author: Maurice Haro
"""


from models.base import Base


class Rectangle(Base):
    """
    models a rectanlge with sides and position

    Attributes:
        width (int): width of the rectangle
        height (int): height of the rectangle
        x (int): x-position
        y (int): y-position
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializing instance attributes

        Args:
        width (int): width of the rectangle
        height (int): height of the rectangle
        x (int): x-position
        y (int): y-position
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def validator(self, name, value):
        """
        validates input for the rectangle parameters

        Arguments:
            param (str): the rectangle attribute to validate
            value (int): the value to validate
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if (name == 'width' or name == 'height') and value <= 0:
            raise ValueError("{} must be > 0".format(name))
        if (name == 'x' or name == 'y') and value < 0:
            raise ValueError("{} must be >= 0".format(name))

    @property
    def width(self):
        """
        Returns the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle
        """
        self.validator("width", value)
        self.__width = value

    @property
    def height(self):
        """
        Returns the height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle
        """
        self.validator("height", value)
        self.__height = value

    @property
    def x(self):
        """
        Returns the x-position of the rectangle
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Sets the x-position of the rectangle
        """
        self.validator("x", value)
        self.__x = value

    @property
    def y(self):
        """
        Returns the y-position of the rectangle
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Sets the y-position of the rectangle
        """
        self.validator("y", value)
        self.__y = value

    def area(self):
        """
        Calculates the area of a given rectangle

        Returns: the area of the rectangle
        """
        return self.width * self.height

    def display(self):
        """
        Displays rectangle representation to stdout using # character
        """
        for i in range(self.y):
            print()
        for i in range(self.height):
            for j in range(self.x):
                print(' ', end='')
            for j in range(self.width):
                print('#', end='')
            print()

    def __str__(self):
        """
        override the __str__() method to print in format

        Returns:
            formated string representation
                """
        string = "[{}] ({}) {}/{} - {}/{}".format(
                self.__class__.__name__, self.id, self.x, self.y,
                self.width, self.height)
        return string

    def update(self, *args, **kwargs):
        """
        Assigns an argument to each attribute of the rectangle

        Arguments:
            *args: the arguments list privided by user
        """
        if args is not None and len(args) != 0:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.width = arg
                elif i == 2:
                    self.height = arg
                elif i == 3:
                    self.x = arg
                elif i == 4:
                    self.y = arg

        elif kwargs is not None and len(kwargs) != 0:
            for (key, value) in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """
        Returns a dict representation of the square object
        """
        return {"id": self.id, "width": self.width, "height": self.height,
                "x": self.x, "y": self.y}
