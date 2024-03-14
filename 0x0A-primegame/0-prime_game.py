#!/usr/bin/python3
"""
0-prime_game module
"""


def isWinner(x, nums):
    """ Returns the winner of the prime game """
    if type(nums) is not list or len(nums) == 0:
        return None

    mariaCount = 0
    benCount = 0
    gameRound = 0
    while gameRound < x and gameRound < len(nums):
        n = nums[gameRound]
        primeCount = numberOfPrimes(n)

        if primeCount % 2 == 0:
            benCount += 1
        else:
            mariaCount += 1

        gameRound += 1

    if benCount > mariaCount:
        return "Ben"
    elif benCount < mariaCount:
        return "Maria"


def numberOfPrimes(n):
    """ Returns the number of prime numbers found starting from 1 upto n """
    count = 0
    for i in range(2, n + 1):
        if isPrime(i):
            count += 1
    return count


def isPrime(n):
    """ Checks if a numvber is prime """
    for i in range(2, n // 2):
        if n % i == 0:
            return False
    return True
