#!/usr/bin/python3
"""Coin Change Problem Module
"""

from typing import List


def makeChange(coins: List[int], total: int) -> int:
    """return the fewest number of coins needed to meet the total
    """
    rs = [total+1] * (total+1)
    rs[0] = 0
    for i in xrange(1, total+1):
        for c in coins:
            if i >= c:
                rs[i] = min(rs[i], rs[i-c] + 1)

    if rs[total] == total+1:
        return -1
    return rs[total]
