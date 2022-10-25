#!/usr/bin/python3
"""
save_to_json_file function: writes an object to a text file using JSON rep

Created on Tue Oct, 25 2022

@author: Maurice Haro
"""
import json


def save_to_json_file(my_obj, filename):
    """
    writes an object to a text file using JSON representation
    """

    with open(filename, mode='w', encoding='utf-8') as f:
        return f.write(json.dumps(my_obj))
