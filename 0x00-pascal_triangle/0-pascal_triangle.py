#!/usr/bin/python3
""" Pascal's Triangle """
from math import factorial


def pascal_triangle(n):
    """  returns a list of lists of integers
    representing the Pascals triangle of n"""
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            ncr = factorial(i) // (factorial(j) * factorial(i - j))
            row.append(ncr)
        triangle.append(row)
    return triangle
