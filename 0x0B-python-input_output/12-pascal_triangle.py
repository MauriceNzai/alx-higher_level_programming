#!/usr/bin/python3
"""
Module consists of a function that returns the pascal triangle

Created on Wed Oct, 26 2022

@author: Maurice Haro
"""


def pascal_triangle(n):
    """
    Returns the pascal triangle

    Args:
        n (int): number of lines

    Returns: A matrix with the pascal triangle
    """

    matrix = []
    prev = []

    for i in range(n):
        my_list = []
        p1 = -1
        p2 = 0

        for j in range(len(prev) + 1):
            if p1 == -1 or p2 == len(prev):
                my_list += [1]
            else:
                my_list += [prev[p1] + prev[p2]]

            p1 += 1
            p2 += 1

        matrix.append(my_list)
        prev = my_list[:]

    return matrix
