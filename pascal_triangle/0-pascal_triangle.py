#!/usr/bin/python3
"""Pascal's Triangle module."""


def pascal_triangle(n):
    """Return Pascal's Triangle with n rows."""
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        row = [1]

        if i > 0:
            previous_row = triangle[i - 1]

            for j in range(1, i):
                row.append(previous_row[j - 1] + previous_row[j])

            row.append(1)

        triangle.append(row)

    return triangle
