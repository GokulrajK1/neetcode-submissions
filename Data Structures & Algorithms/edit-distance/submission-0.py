class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[float('inf')] * (n + 1) for _ in range(m +1)]
        dp[m][n] = 0
        for i in range(m):
            dp[i][n] = m - i
        for j in range(n):
            dp[m][j] = n - j

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if word1[i] == word2[j]:
                    print(i,j)
                    print("sub", 1 + dp[i + 1][j + 1])
                    print("delete", 1 + dp[i + 1][j])
                    print("add", 1 + dp[i][j + 1])
                    dp[i][j] = min(dp[i + 1][j + 1], 1 + dp[i + 1][j], 1 + dp[i][j +1])
                else:
                    print(i,j)
                    print("sub", 1 + dp[i + 1][j + 1])
                    print("delete", 1 + dp[i + 1][j])
                    print("add", 1 + dp[i][j + 1])
                    dp[i][j] = min(1 + dp[i + 1][j + 1], 1 + dp[i + 1][j], 1 + dp[i][j + 1]) 
        for row in dp:
            print(row)
        return dp[0][0]