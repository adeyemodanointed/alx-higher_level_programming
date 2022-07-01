#!/usr/bin/python3
"""

"""

def matrix_divided(matrix, div):
    """ """
    length = len(matrix[0])
    for row in matrix:
        if(type(row) is not list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        for column in row:
            if(type(column) is not float and type(column) is not int):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if(len(row) != length):
            raise TypeError("Each row of the matrix must have the same size")
    if(type(div) != float and type(div) != int):
        raise TypeError("div must be a number")
    if(div == 0):
        raise ZeroDivisionError("division by zero")
    return [[round(i/div, 2) for i in l] for l in matrix]
