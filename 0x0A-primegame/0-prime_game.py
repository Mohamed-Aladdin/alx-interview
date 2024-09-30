#!/usr/bin/python3
"""Prime Game Module"""


def isWinner(x, nums):
    """Return the name of the player that won the most rounds
    """
    if x < 1 or not nums:
        return None
    ben, maria = 0, 0
    results = {}

    for num in nums:
        if num in results:
            ben, maria = results[f"{num}"]
        else:
            if num < 2:
                ben += 1
            else:
                primes = 0

                for i in range(2, num + 1):
                    if i == 2 or i == 3 or i == 5:
                        primes += 1
                        continue
                    if i % 2 != 0 and i % 3 != 0 and i % 5 != 0:
                        primes += 1
                if primes % 2 == 0:
                    ben += 1
                else:
                    maria += 1
                results[f"{num}"] = (ben, maria)

    if ben > maria:
        return "Ben"
    elif ben == maria:
        return None
    else:
        return "Maria"
