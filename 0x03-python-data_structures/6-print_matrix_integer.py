#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for list_t in matrix:
        for idx in range(len(list_t)):
            print(" ".join("{:d}").format(list_t[idx])))
