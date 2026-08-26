class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        # dp = [float("inf")] * (amount + 1)
        # dp[0] = 0 
        # for a in range(1, amount+1):
        #     for c in coins:
        #         if a - c >= 0:
        #             dp[a] = min(dp[a], 1 + dp[a - c])

        # return -1 if dp[amount] == float("inf") else dp[amount]

        memo = {}

        def backtrack(total):
            if total in memo:
                return memo[total]

            if total < 0:
                return float("inf")

            if total == 0:
                return 0
            res = float("inf")
            for c in coins:
                res = min(res, 1 + backtrack(total - c))

            memo[total] = res

            return res

        ans = backtrack(amount)
        return -1 if ans == float("inf") else ans

        
                
                


            
