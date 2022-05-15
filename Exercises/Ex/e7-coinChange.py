# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
# You may assume that you have an **infinite** number of each kind of coin.

# Input: coins = [1, 5, 2], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
# https://www.youtube.com/watch?v=H9bfqozjoqs

# Time Complexity: O(mAmount * len(coinsArr))

coinsArr = [11, 5, 2]
amount = 20


def coinsChange(mCoinsArr, mAmount):

    if mAmount <= 0 or len(mCoinsArr) == 0:
        return -1

    coinsArr.sort()
    # [max coin can (can also float('inf'))] * size of mAmount
    # so if amount is 4 > [5,5,5,5,5] we going from 0 -> 4
    dp = [mAmount + 1] * (mAmount + 1)

    dp[0] = 0  # computed 0 so in forLoop start 1

    for computedAmount in range(1, mAmount + 1):
        for coin in mCoinsArr:
            if computedAmount - coin >= 0:
                dp[computedAmount] = min(
                    # if we at coin 4 and we need amount 7 ,so dp[7] = 1 + dp[ 7 - 4] // we use one coin 4 and left 7-4
                    dp[computedAmount], 1 + dp[computedAmount - coin])
    return dp[mAmount] if dp[mAmount] != mAmount + 1 else -1


print(coinsChange(coinsArr, amount))
