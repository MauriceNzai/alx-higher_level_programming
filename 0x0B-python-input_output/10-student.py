#!/usr/bin/python3
"""
Module to define the class Student

Created on Wed Oct, 26 2022

@author: Maurice Haro
"""


class Student:
    """
    Defines student by publice instance variables

    Attributes:
        first_name (str): Student's first name
        last_name (str): student's last name
        age (int): student's age
    """
    def __init__(self, first_name, last_name, age):
        """
        initialize public instance variables

        Argument:
            first_name (str): Student's first name
            last_name (str): student's last name
            age (int): student's age
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrieves a dictionary representation of  a Student

        Return: dictionary representation
        """
        my_obj = self.__dict__.copy()
        if (type(attrs) is list):

            for item in attrs:
                if (type(item)) is not str:
                    return my_obj

            dict_list = {}

            for item_attr in range(len(attrs)):
                for str_attr in my_obj:
                    if attrs[item_attr] == str_attr:
                        dict_list[str_attr] = my_obj[str_attr]
            return dict_list

        return my_obj
