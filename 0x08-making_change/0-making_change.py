#!/usr/bin/python3
"""
0-making_change module
"""


def makeChange(coins, total):
	""" Determines the fewest number of coins needed to meet
	a given amount total """
	if total <= 0:
		return 0
	remainder = total
	count = 0
	index = 0
	sorted_coins = sorted(coins, reverse=True)
	length = len(coins)
	while remainder > 0:
        if index >= length:
            return -1
        if 0 <= remainder - sorted_coins[index]:
            remainder -= sorted_coins[index]
            count += 1
        else:
            index += 1
    return count
