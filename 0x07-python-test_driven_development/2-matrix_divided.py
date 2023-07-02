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
    if not all(isinstance(row, list) and all(isinstance(value, (int, float))
               for value in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/float")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return ([list(map(lambda x: round(x / div, 2), y)) for y in matrix])
