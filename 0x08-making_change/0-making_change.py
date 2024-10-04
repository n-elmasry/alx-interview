#!/usr/bin/python3
"""makeChange"""


def makeChange(coins, total):
    """determine the fewest number of coins
    needed to meet a given amount total"""
    if total == 0:
        return 0
    if coins == [] or coins is None:
        return -1
    dp = [total + 1] * (total + 1)

    dp[0] = 0

    for coin in coins:
        for i in range(coin, total+1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != total + 1 else -1
