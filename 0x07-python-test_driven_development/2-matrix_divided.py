#!/usr/bin/python3

"""
This module provides a function to divide
all elements of a matrix by a given number.

The function ensures that:
- The matrix is a list of lists of integers or floats.
- All rows in the matrix are of the same size.
- The divisor is a number (integer or float) and is not zero.
"""


def matrix_divided(matrix, div):

    """
    Divides all elements of a matrix by a given
    divisor and returns a new matrix with the results.

    Args:
        matrix (list of list of int/float): A matrix to be divided,
        where each row must contain int or float types.
        div (int/float): The number by
        which to divide each element of the matrix.

    Raises:
        TypeError: If the matrix is not a list of lists of integers or floats.
        TypeError: If any element of the matrix is not an integer or float.
        TypeError: If the rows of the matrix are not all of the same size.
        TypeError: If the divisor is not a number (integer or float).
        ZeroDivisionError: If the divisor is zero.

    Returns:
        list of list of float: A new matrix with all elements
        divided by the divisor, rounded to 2 decimal places.
    """
    if not isinstance(matrix, list) or not all(
                      isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix
                        (list of lists) of integers/floats")

    for row in matrix:
        if not all(isinstance(element, (int, float)) for element in row):
            raise TypeError("matrix must be a matrix
                            (list of lists) of integers/floats")

    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(element / div, 2) for element in row] for row in matrix]
