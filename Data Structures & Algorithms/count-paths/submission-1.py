class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        # def backtrack(i, j, memo):

        #     if (i, j) in memo:
        #         return memo[(i, j)]

        #     if i == m - 1 and j == n - 1:
        #         return 1 

        #     if i < 0 or i >= m or j < 0 or j >= n:
        #         return 0 

        #     down = backtrack(i + 1, j, memo)
        #     right = backtrack(i, j + 1, memo)

        #     memo[(i + 1, j)] = down
        #     memo[(i, j + 1)] = right 

        #     return down + right 


        # return backtrack(0, 0, {})

        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            dp[i][n - 1] = 1

        for j in range(n):
            dp[m - 1][j] = 1

        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                dp[i][j] = dp[i + 1][j] + dp[i][j + 1]

        return dp[0][0]
