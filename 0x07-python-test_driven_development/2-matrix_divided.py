#!/usr/bin/python3
'''
A function that divides all elements of a matrix.
It must be list of list and each row must contain int or float type
'''


def matrix_divided(matrix, div):

    '''
    Check if matrix is a list of lists of integers or floats
    Check if all elements in the matrix are integers or floats
    Check if all rows are of the same size
    Check if div is a number
    Check if div is zero
    THEN
    Perform the division and return a new matrix
    '''

    if not isinstance(matrix, list) or not all(
            isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix
                        (list of lists) of integers/floats")
    for rw in matrix:
        if not all(isinstance(element, (int, float)) for element in row):
            raise TypeError("matrix must be a matrix
                            (list of lists) of integers/floats")

    r_len = len(matrix[0])
    if not all(len(row) == r_len for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    matrixx = []
    for row in matrix:
        new_row = [round(element / div, 2) for element in row]
        matrixx.append(new_row)

    return matrixx
