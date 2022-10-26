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
        self.age =  age

        def to_json(self):
            """
            retrieves a dictionary representation of  a Student

            Return: dictionary representation
            """
            return (self.__dict__.copy())

