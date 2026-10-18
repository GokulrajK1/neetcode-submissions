class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for i in range(len(coins)):
            for target in range(1, amount + 1):
                if target < coins[i]: continue
                dp[target] += dp[target - coins[i]]

        return dp[amount]