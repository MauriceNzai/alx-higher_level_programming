#!/usr/bin/python3
"""
load_from_json_file function: Creates an object from a JSON file

Created on Tue Oct, 25 2022

@author: Maurice Haro
"""
import json


def load_from_json_file(filename):
    """
     Loads an object from JSON file

     Arguments:
        filename (str): Name of the file

    Return:
        A file with the text in JSON format
    """

    with open(filename, mode='r', encoding='utf-8') as f:
        return (json.loads(f))
