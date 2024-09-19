#!/usr/bin/python3
"""Coin Change Problem Module
"""

from typing import List


def makeChange(coins: List[int], total: int) -> int:
    """return the fewest number of coins needed to meet the total
    """
    def coinChange(self, coins, amount):
        MAX = float('inf')
        dp = [0] + [MAX] * amount

        for i in xrange(1, amount + 1):
            dp[i] = min([dp[i - c] if i - c >= 0 else MAX for c in coins]) + 1

        return [dp[amount], -1][dp[amount] == MAX]
