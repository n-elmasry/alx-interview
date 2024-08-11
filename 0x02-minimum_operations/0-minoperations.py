#!/usr/bin/python3
"""minOperations"""
import math


def minOperations(n: int) -> int:
    """calculates the fewest number of operations needed
    to result in exactly n H characters in the file."""
    minop = 0

    if n <= 1:
        return 0

    while n % 2 == 0:
        n = n // 2
        minop += 1

    for i in range(3, int(math.sqrt(n))+1, 2):
        while n % i == 0:
            n = n // i
            minop += i
    if n > 2:
        minop += n

    return minop
