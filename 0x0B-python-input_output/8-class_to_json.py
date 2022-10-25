#!/usr/bin/python3
"""
Module that creates a function returning a dictionary description

Created on Tue Oct, 25 2022

@author: Maurice Haro
"""


def clas_to_json(obj):
    """
    Creates a JSON representation of an object

    Argumente:
        obj (obj): The object to create a class of


    Return:
        A JSON representation
    """
    dic = {}
    if hasattr(obj, "__dict__"):
        dic = obj.__dict__.copy()
    reurn dic
