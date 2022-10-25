#!/usr/bin/python3
"""
MyInt class
Created on Tue oct, 25 2022

@author: Maurice Haro
"""


class MyInt(int):
    """
    Inherits from int
    """

    def __eq__(self, num):
        """
        equal method to do opposite of parent class

        Attributes:
            num (int): integer value

        Returns:
            The oposite boolean value of the value
        """

        return (int(self) != num)

    def __ne__(self, num):
        """
        not equal method to do opposite of parent class

        Attributes:
            num (int): integer value

        Returns:
            The oposite boolean value of the value
        """

        return (int(self) == num)
