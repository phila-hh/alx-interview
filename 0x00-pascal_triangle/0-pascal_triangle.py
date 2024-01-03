#!/usr/bin/python3
"""This module contains the pascal_triangle function"""

def pascal_triangle(n):
    """Returns a list of lists of integers representing the Pascal's
    triangle of n"""
    pasTriList = []
    m = 1

    if n <= 0:
        return pasTriList

    for i in range(0, n):
        lst = []
        rc_even, rc_odd = 1, 2
        if i == 0:
            lst = [1]
        elif i == 1:
            lst = [1, 1]
        else:
            for j in range(0, m):
                if j == 0 or j == (m - 1):
                    lst.append(1)
                else:
                    lst.append(pasTriList[i-1][j] + pasTriList[i-1][j-1])

        pasTriList.append(lst)
        m += 1

    return pasTriList
