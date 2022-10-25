#!/usr/bin/python3
"""
write_file function writes to a text file and
returns number of characters written

Created on Tue Oct, 25 2022

@author: Maurice Haro
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file
    Creates the file if it does not exist
    Overwrites the content of the file if it already exists
    """

    with open(filename, mode='w', encoding='utf-8') as f:
        return(f.write(text))
