#!/usr/bin/python3
"""
Module contains a function that appends a line of text after a given string

Created on Wed Oct, 26 2022

@author: Mauroce Haro
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Append a line of text to a file, after each line containing a given string

    Attributes:
        filename (str): the name of the file to insert into
        search_string (str): the string of text after which to insert
        new_string (str): the string to insert
    """

    text = []
    with open(filename, mode='r', encoding='utf-8') as f:
        for line in f:
            text += [line]

            if line.find(search_string) != -1:
                text += [new_string]

    with open(filename, mode='w', encoding='utf-8') as f:
        f.write("".join(text))
