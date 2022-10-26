#!/usr/bin/python3
"""
function read_file to read a file and display on stdo
Created on Tue Oct, 25 2022

@author: Maurice Haro
"""


def read_file(filename=""):
    """reads a file"""
    with open(filename, mode='r', encoding='utf-8') as f:
        for line in f:
            print(line, end="")
