#!/usr/bin/python3
"""
    0-minimum_operations module
"""


def minOperations(n):
    """Calculates the fewest number of oprations needed"""
    if type(n) is not int:
        return 0
    count = 0
    clipboard = 0
    done = 1
    while n > done:
        if clipboard == 0:
            clipboard = done
            done += clipboard
            count += 2
        elif (n - done) % done == 0 and n - done > 0:
            clipboard = done
            done += clipboard
            count += 2
        elif clipboard > 0:
            done += clipboard
            count += 1

    return count
