#!/usr/bin/python3
"""
The module prints text with 2 new lines after the characters ., ? and :

Created on Tue Oct 18 2022
@author: Maurice Haro
"""


def text_indentation(text):
    """
    prints given text inserting two new lines after the '.', '?' and ':' chars

    Args:
        text (str): The text to print

    Raises:
        TypeError: Exception if text is not string
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    new_text = text.replace('.', '.\n\n').replace(':', ':\n\n')\
            .replace('?', '?\n\n')
    for i in range(len(text)):
        new_text = new_text.replace('\n', '\n')

    print(new_text, end="")
