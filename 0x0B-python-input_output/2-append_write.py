#!/usr/bin/python3
"""
write_file function writes to a text file and
returns number of characters written

Created on Tue Oct, 25 2022

@author: Maurice Haro
"""


def append_write(filename="", text=""):
    """
    Writes a string to a text file
    Creates the file if it does not exist
    Appends the content of the file if it already exists
    """

    with open(filename, mode='a+', encoding='utf-8') as f:
        return(f.write(text))
