#!/usr/bin/python3
"""Solve the N Queens puzzle using backtracking."""

import sys


def is_safe(queens, row, col):
    """Check whether a queen can be placed safely."""
    for queen in queens:
        prev_row, prev_col = queen

        if prev_col == col:
            return False

        if abs(prev_row - row) == abs(prev_col - col):
            return False

    return True


def solve_nqueens(n, row, queens):
    """Find and print all valid queen arrangements."""
    if row == n:
        print(queens)
        return

    for col in range(n):
        if is_safe(queens, row, col):
            queens.append([row, col])
            solve_nqueens(n, row + 1, queens)
            queens.pop()


def main():
    """Validate arguments and solve the N Queens puzzle."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(n, 0, [])


if __name__ == "__main__":
    main()

