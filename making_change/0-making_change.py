#!/usr/bin/python3
"""Find the minimum number of coins needed to make change."""


def makeChange(coins, total):
    """Return the minimum number of coins needed for the total."""
    if total <= 0:
        return 0

    dp = [total + 1] * (total + 1)
    dp[0] = 0

    for amount in range(1, total + 1):
        for coin in coins:
            if coin <= amount:
                dp[amount] = min(
                    dp[amount],
                    dp[amount - coin] + 1
                )

    if dp[total] == total + 1:
        return -1

    return dp[total]
