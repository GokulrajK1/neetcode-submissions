import math

class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for amount in range(1, n + 1):
            for i in range(1, int(math.sqrt(n)) + 1):
                if amount < i * i: 
                    break 
                dp[amount] = min(dp[amount], 1 + dp[amount - i * i])

        return dp[n]
