#!/usr/bin/python3
"""
0-validate_utf8 module
"""


def validUTF8(data):
    """Validates if a list of integers are UTF8"""
    jump = 0
    n = len(data)
    for i in range(n):
        if jump > 0:
            jump -= 1
            continue
        if type(data[i]) is not int or data[i] < 0 or data[i] > 0x10ffff:
            return False
        elif data[i] <= 0x7f:
            jump = 0
        elif data[i] & 0b11111000 == 0b11110000:
            width = 4
            if n - i >= width:
                next_body = list(map(
                    lambda x: x & 0b11000000 == 0b10000000,
                    data[i + 1: i + width]
                ))
                if not all(next_body):
                    return False
                jump = width - 1
            else:
                return False
        elif data[i] & 0b11110000 == 0b11100000:
            width = 3
            if n - i >= width:
                next_body = list(map(
                    lambda x: x & 0b11000000 == 0b10000000,
                    data[i + 1: i + width]
                ))
                if not all(next_body):
                    return False
                jump = width - 1
            else:
                return False
        elif data[i] & 0b11100000 == 0b11000000:
            width = 2
            if n - i >= width:
                next_body = list(map(
                    lambda x: x & 0b11000000 == 0b10000000,
                    data[i + 1: i + width]
                ))
                if not all(next_body):
                    return False
                jump = width - 1
            else:
                return False
        else:
            return False
    return True
