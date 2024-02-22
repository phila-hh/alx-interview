#!/usr/bin/python3
"""
Rotate 2d matrix module
"""


def rotate_2d_matrix(matrix):
    """ Rotates a 2d matrix in place """
    length = len(matrix)

    for i in range(length):
        for j in range(i, length):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(length):
        matrix[i].reverse()
