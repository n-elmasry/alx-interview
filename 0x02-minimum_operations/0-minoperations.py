#!/usr/bin/python3
"""minOperations"""


def minOperations(n: int) -> int:
    """calculates the fewest number of operations needed
    to result in exactly n H characters in the file."""
    opnum = 0
    minop = 2

    if n <= 1:
        return 0

    while n > 1:
        while n % minop == 0:
            opnum += minop
            n //= minop
        minop += 1
    return opnum
