#!/usr/bin/python3
"""Task 0 Module"""

import sys


def validate_input() -> int:
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit():
        n = int(sys.argv[1])
    else:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return n

def n_queens() -> None:
    n = validate_input()
    col = set()
    posDiag = set() #(r + c) is always constant
    negDiag = set() #(r - c) is always constant
    sol = []
    result = []

    def backtrack(r: int) -> None:
        if r == n:
            copy = sol.copy()
            result.append(copy)
            return
        for c in range(n):
            if c in col or (r + c) in posDiag or (r - c) in negDiag:
                continue
            col.add(c)
            posDiag.add(r + c)
            negDiag.add(r - c)

            sol.append([r, c])
            backtrack(r + 1)

            col.remove(c)
            posDiag.remove(r + c)
            negDiag.remove(r - c)
            sol.remove([r, c])

    backtrack(0)
    for solution in result:
        print(solution)


if __name__ == '__main__':
    n_queens()
