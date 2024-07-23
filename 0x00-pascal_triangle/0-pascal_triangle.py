#!/usr/bin/python3
"""determine pascal's triangle"""


def pascal_triangle(n):
    """
    returns a list of lists of ints representing Pascal’s triangle
    """

    triangle = []

    if n <= 0:
        return triangle

    for i in range(n):
        temp_ls = []

        for j in range(i + 1):
            if j == i or j == 0:
                temp_ls.append(1)
            else:
                temp_ls.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        triangle.append(temp_ls)
    return triangle
