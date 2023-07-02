#!/usr/bin/python3
""""Module that divides each element in a string by 3"""


def matrix_divided(matrix, div):
    """
    matix_divided - mudole divides all elements of a matrix
    @matrix: list of integers
    @div: integer to divide by
    Return: new matrix

    Raise:
    TypeError: if number not int 
    or matrix row not the same size
    ZeroDivisionError: if div is 0
    """
    if not all(isinstance(row, list) and all(isinstance(value, int))
            or all(isinstance(value, float) for value in row) 
            for row in matrix):

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return ([list(map(lambda x: round(x / div, 2), y)) for y in matrix])
