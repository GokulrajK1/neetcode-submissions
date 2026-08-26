class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        # Top Down
        # n = len(coins)
        
        # def backtrack(i, remaining, memo):

        #     if (i, remaining) in memo:
        #         return memo[(i, remaining)]

        #     if remaining == 0:
        #         return 1 

        #     if remaining < 0:
        #         return 0 

        #     if i == n:
        #         return 0 

        #     memo[(i, remaining - coins[i])] = backtrack(i, remaining - coins[i], memo) 
        #     memo[(i + 1, remaining)] = backtrack(i + 1, remaining, memo)

        #     return memo[(i, remaining - coins[i])] + memo[(i + 1, remaining)]

        # return backtrack(0, amount, {})


        # Bottom Up 
        n = len(coins)
        dp = [[0] * (n + 1) for _ in range(amount + 1)]
        for i in range(n): 
            dp[0][i] = 1 

        for a in range(1, amount + 1):
            for i in range(n - 1 , -1, -1):
                dp[a][i] = dp[a - coins[i]][i] + dp[a][i + 1]

        return dp[amount][0]
