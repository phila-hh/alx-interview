#!/usr/bin/python3
"""
0-prime_game module
"""


def isWinner(x, nums):
    """ Returns the winner of the prime game """
    if type(nums) is not list or not nums or x < 1:
        return None

    mariaCount = 0
    benCount = 0
    gameRound = 0
    while gameRound < x and gameRound < len(nums):
        n = nums[gameRound]
        primeCount = 0
        for i in range(2, n + 1):
            isPrime = True
            for j in range(2, i // 2):
                if i % j == 0:
                    isPrime = False
                    break
            if isPrime is True:
                primeCount += 1

        if primeCount % 2 == 0:
            benCount += 1
        else:
            mariaCount += 1

        gameRound += 1

    if benCount > mariaCount:
        return "Ben"
    elif benCount < mariaCount:
        return "Maria"
    else:
        return None
