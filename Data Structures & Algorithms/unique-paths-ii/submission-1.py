class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[m - 1][n - 1] = 1 if obstacleGrid[m - 1][n -1] == 0 else 0
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if obstacleGrid[i][j] == 1: continue
                if i == m - 1 and j == n - 1: continue 
                dp[i][j] = dp[i + 1][j] + dp[i][j + 1]

        return dp[0][0]