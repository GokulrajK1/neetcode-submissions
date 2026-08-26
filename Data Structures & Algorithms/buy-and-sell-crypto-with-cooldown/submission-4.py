class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # n = len(prices)
        
        # def backtrack(i, can_buy, memo):

        #     if (i, can_buy) in memo:
        #         return memo[(i, can_buy)]
            
        #     if i >= n:
        #         return 0 
            
        #     buying = selling = 0
        #     if can_buy:
        #         buying = -prices[i] + backtrack(i + 1, False, memo)
        #     else:
        #         selling = prices[i] + backtrack(i + 2, True, memo)

        #     memo[(i, can_buy)] = max(buying, selling, backtrack(i + 1, can_buy, memo))
        #     return memo[(i, can_buy)]


        # return backtrack(0, True, {})

        n = len(prices)
        dp = [[0, 0] for _ in range(n+1)]
        for i in range(n - 1, -1, -1):
            for buying in [True, False]:
                if buying:
                    buy = -prices[i] + dp[i + 1][False]
                    cooldown = dp[i + 1][True]
                    dp[i][True] = max(buy, cooldown)
                else:
                    sell = prices[i] + dp[i + 2][True] if i + 2 < n else prices[i]
                    cooldown = dp[i + 1][False]
                    dp[i][False] = max(sell, cooldown)

        return dp[0][True]
            

