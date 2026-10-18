class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0, 0] for _ in range(n + 2)]

        for i in range(n - 1, -1, -1):
            for can_buy in [True, False]:
                if can_buy:
                    dp[i][can_buy] = max(-prices[i] + dp[i+1][not can_buy], dp[i+1][can_buy])
                else:
                    dp[i][can_buy] = max(dp[i+1][can_buy], prices[i] + dp[i + 2][not can_buy])


        return min(dp[0][0], dp[0][1])