#!/usr/bin/python3
"""
load_from_json_file function: Creates an object from a JSON file

Created on Tue Oct, 25 2022

@author: Maurice Haro
"""
import json


def load_from_json_file(filename):
    """
    Function that creates an Object from a JSON file
    Args:
        filename: textfile name
    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
