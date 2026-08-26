class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Top Down DP
        # n = len(coins)
        # def backtrack(i, curr, num, memo):
        #     nonlocal amount
        #     if curr > amount:
        #         return -1 

        #     if curr == amount:
        #         return num 

        #     if i == n:
        #         return -1 

        #     res = -1

        #     if (i, curr, num) in memo:
        #         return memo[(i, curr, num)]

        #     if coins[i] + curr <= amount:
        #         res = backtrack(i, curr + coins[i], num + 1, memo)

        #     x = backtrack(i + 1, curr, num, memo)

        #     if res == -1:
        #         memo[(i, curr, num)] = x
        #         return x 

        #     if x == -1:
        #         memo[(i, curr, num)] = res
        #         return res

        #     memo[(i, curr, num)] = min(res, x)
            
        #     return min(res, x)

        # return backtrack(0, 0, 0, {})

        # Bottom Up DP
        n = len(coins)
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for j in range(n):
                if coins[j] <= i:
                    dp[i] = min(dp[i], 1 + dp[i - coins[j]])

        return dp[amount] if dp[amount] != float("inf") else -1