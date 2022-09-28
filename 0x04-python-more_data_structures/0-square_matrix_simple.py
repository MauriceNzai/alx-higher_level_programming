#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    my_matrix = matrix
    my_matrix = [[i ** 2 for i in my_sublist] for my_sublist in my_matrix]
    return(my_matrix)
