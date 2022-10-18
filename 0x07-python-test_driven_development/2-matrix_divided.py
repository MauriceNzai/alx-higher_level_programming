#!/usr/bin/python3
"""
This module consists of a matrix divider function

Created on Tue Oct 18 2022
@author Maurice Haro
"""
def matrix_divided(matrix, div):
    """
    Divides all the elements of a matrix by div

    Attributes:
        matrix: The matrix whose elements are to be divided
    
        div: The integer to divide elements by

    Raises:
        TypeError: If not list of lists of integers or floats\
                rows not same size
                div not integer or float
        ZeroDivisionError: If div is 0

    Returns:
        new_matrix: Same size as matrix with elements divided by div\
                and rounded to 2 decimal places
    """
    if type(div) not in [int, float] or div != div:
        raise TypeError("div must be a number")
        return matrix
    elif div == 0:
        raise ZeroDivisionError("division by zero")
        return matrix

    if type(matrix) is list:
        new_matrix = [x[:] for x in matrix]
        for i in range(len(matrix)):
            if i <= len(matrix) - 2 and len(matrix[i]) != len(matrix[i + 1]):
                raise TypeError("Each row of the matrix must have the\
                        same size")
                return matrix
            for j in range(len(matrix[i])):
                if type(matrix[i][j]) not in [int, float] or\
                        matrix[i][j] != matrix[i][j]:
                    raise TypeError("matrix must be a matrix (list of lists)\
                            of integers/floats")
                    return matrix
                else:
                    new_matrix[i][j] = round(matrix[i][j] / div, 2)

    else:
        raise TypeError("matrix must be a matrix (list of lists)\
                of integers/floats")
        return matrix
        
    return new_matrix
