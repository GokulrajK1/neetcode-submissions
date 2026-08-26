class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        m, n = len(matrix), len(matrix[0])

        def dfs(i, j, dp):
            if i < 0 or i >= m or j < 0 or j >= n:
                return 0 
            

            if dp[i][j] != 0:
                return dp[i][j]

            res = 1

            if i > 0 and matrix[i][j] < matrix[i - 1][j]:
                res = max(res, 1 + dfs(i - 1, j, dp))

            if i < m - 1 and matrix[i][j] < matrix[i + 1][j]:
                res = max(res, 1 + dfs(i + 1, j, dp))

            if j > 0 and matrix[i][j] < matrix[i][j - 1]:
                res = max(res, 1 + dfs(i, j - 1, dp))

            if j < n - 1 and matrix[i][j] < matrix[i][j + 1]:
                res = max(res, 1 + dfs(i, j + 1, dp))

            dp[i][j] = res

            return res
        
        max_path = 1
        dp = [[0] * (n) for _ in range(m)]
        for i in range(m):
            for j in range(n):
                max_path = max(max_path, dfs(i, j, dp))

     
        return max_path

                 

            
