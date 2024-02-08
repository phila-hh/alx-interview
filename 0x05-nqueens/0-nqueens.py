#!/usr/bin/python3
"""
0-nqueens module
"""
import sys


def nqueens(n):
    """ Solves the N queens problem """
    if not n.isdigit():
        print("N must be a number")
        sys.exit(1)

    n = int(n)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * n
    solve(board, 0, n)


def solve(board, row, n):
    """ Explores all possible configurations of placing queen on the board """
    if row == n:
        print([[i, board[i]] for i in range(n)])
        return

    for column in range(n):
        if is_safe(board, row, column):
            board[row] = column
            solve_nqueens(board, row + 1, n)


def is_safe(board, row, column):
    """ Checks if it is safe to place the queen in the given location """
    for i in range(row):
        if (board[i] == column) or \
           (board[i] - i == column - row) or \
           (board[i] + i == column + row):
            return False
    return True


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    nqueens(sys.argv[1])
