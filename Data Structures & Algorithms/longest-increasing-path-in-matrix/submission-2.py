class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        m, n = len(matrix), len(matrix[0])

        memo = {}
        
        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
                
            if i < 0 or j < 0 or i >= m or j >= n:
                return 0 

            up = down = left = right = 0
            if i - 1 >= 0 and matrix[i][j] < matrix[i - 1][j]:
                up = dfs(i - 1, j)
            if i + 1 < m and matrix[i][j] < matrix[i + 1][j]:
                down = dfs(i + 1, j)
            if j - 1 >= 0 and matrix[i][j] < matrix[i][j - 1]:
                left = dfs(i, j - 1)
            if j + 1 < n and matrix[i][j] < matrix[i][j + 1]:
                right = dfs(i, j + 1)

            res = 1 + max(up, down, left, right)

            memo[(i, j)] = res

            return res

        max_length = 0

        for i in range(m):
            for j in range(n):
                max_length = max(max_length, dfs(i, j))

        return max_length
            

