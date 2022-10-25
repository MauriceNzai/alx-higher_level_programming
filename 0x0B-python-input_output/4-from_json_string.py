#!/usr/bin/python3
"""
from_json_string function that returns an object (Python data structure)
represented by a JSON string

Created on Tue Oct, 25 2022

@author: Maurice Haro
"""
import json


def from_json_string(my_str):
    """
    Returns an object represented by a JSON string
    """

    return json.loads(my_str)
