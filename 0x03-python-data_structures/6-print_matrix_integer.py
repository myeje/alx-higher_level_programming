#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in matrix:
        for y in x:
            if y != len(x):
                print("{:d}".format(y), end=' ')
            else:
                print("{:d}".format(y), end='')
        print()
