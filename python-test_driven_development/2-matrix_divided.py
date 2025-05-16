#!/usr/bin/python3
"""
This module provides a function to divide all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number.

    Args:
        matrix (list of lists): A matrix with integers or floats.
        div (int or float): The divisor.

    Returns:
        A new matrix with results rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of ints/floats,
                   or if rows are not the same size,
                   or if div is not a number.
        ZeroDivisionError: If div is zero.
    """
    if (not isinstance(matrix, list) or
            not all(isinstance(row, list) for row in matrix) or
            not all(isinstance(el, (int, float))
                    for row in matrix for el in row)):
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")

    row_lengths = [len(row) for row in matrix]
    if not all(length == row_lengths[0] for length in row_lengths):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(el / div, 2) for el in row] for row in matrix]
