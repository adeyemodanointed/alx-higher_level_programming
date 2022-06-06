#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for list_t in matrix:
        for idx in range(len(list_t)):
            if(idx < len(list_t)-1):
                print("{:d} ".format(list_t[idx]), end=" ")
            else:
                print("{:d}".format(list_t[idx]))
