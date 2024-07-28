#!/usr/bin/python3
""" Pascal's Triangle """


def factorial(n):
    """Calculates the factorial of n (n!)."""
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def pascal_triangle(n):
    """returns a list of lists of integers
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
