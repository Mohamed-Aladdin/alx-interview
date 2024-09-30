#!/usr/bin/python3
"""Prime Game Module"""


def isWinner(x, nums):
    """Return the name of the player that won the most rounds
    """
    maria, ben = 0, 0

    for num in nums:
        if num < 2:
            ben += 1
        else:
            primes = 0

            for i in range(3, num + 1):
                if i == 2 or i == 3:
                    primes += 1
                    continue
                if i % 2 != 0 and i % 3 != 0:
                    primes += 1
            if primes % 2 == 0:
                ben += 1
            else:
                maria += 1
    if ben > maria:
        return "Ben"
    elif ben >= maria:
        return None
    else:
        return "Maria"
