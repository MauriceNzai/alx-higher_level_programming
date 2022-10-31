#!/usr/bin/python3
"""
Square class: Models a square object and inherits Rectangle class

Created on Fri Oct, 28 2022

@author: Maurice Haro
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Models a square object and inherits Rectangle class

    Attributes:
        size (int): the size of the square
        x (int): the x-cordinates of the square
        y (int): the y-coordinates of the square
        id (int): the id of the object/instance
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        initializing the instance attributes

        size (int): the size of the square
        x (int): the x-cordinates of the square
        y (int): the y-coordinates of the square
        id (int): the id of the object/instance
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Returns/gets the size of the square
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        sets the size of the square
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        String representation of the square object
        """
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.size)

    def update(self, *args, **kwargs):
        """
        Assigns the attributes of the square

        Args:
            *args (ints): New attribute values for the square
                -1st arg is the id attribute
                -2nd arg is the size attribute
                -3rd arg is the x attribute
                -4th arg is the y attribute
            **kwargs (dict): New key/value pairs for the square attributes
        """
        if args and len(args) != 0:
            param = 0
            for arg in args:
                if param == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif param == 1:
                    self.size = arg
                elif param == 2:
                    self.x = arg
                elif param == 3:
                    self.y = arg
                param += 1

        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """
        Returns a dict representation of the square object
        """
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
