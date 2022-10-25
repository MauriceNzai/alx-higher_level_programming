#!/usr/bin/python3
"""
to_json_string function that returns JSON representation of an object(string)

Created on Tue Oct, 25 2022

@author: Maurice Haro
"""
import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string)
    """

    return json.dumps(my_obj)
