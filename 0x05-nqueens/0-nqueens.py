#!/usr/bin/python3
"""nqueens"""
import sys
from typing import List


def nqueens() -> None:
    """nqueens"""
    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        sys.exit(1)

    try:
        n = int(sys.argv[1])

    except ValueError:
        print('N must be a number')
        sys.exit(1)

    if n < 4:
        print('N must be at least 4')
        sys.exit(1)

    column = set()
    positive_diagonal = set()
    negative_diagonal = set()

    result = []

    def backtrack(r: int, solution: List[List[int]]) -> None:
        """backtrack"""
        if r == n:
            print(solution)
            return

        for c in range(n):
            if (c in column
                or (r + c) in positive_diagonal
                    or (r - c) in negative_diagonal):
                continue

            column.add(c)
            positive_diagonal.add(r + c)
            negative_diagonal.add(r - c)
            solution.append([r, c])

            backtrack(r + 1, solution)

            column.remove(c)
            positive_diagonal.remove(r + c)
            negative_diagonal.remove(r - c)
            solution.pop()

    backtrack(0, [])


if __name__ == '__main__':
    nqueens()
