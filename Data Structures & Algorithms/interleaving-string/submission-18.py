class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        m, n, o = len(s1), len(s2), len(s3)

        if m + n != o: return False

        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[m][n] = True

        for i in range(m, -1, -1):
            for j in range(n, -1, -1):
                if i == m and j == n: continue
                k = i + j
                dp[i][j] = (i < m and s1[i] == s3[k] and dp[i + 1][j]) or (j < n and s2[j] == s3[k] and dp[i][j + 1])

        return dp[0][0]

        # memo = {}

        # def backtrack(i, j):
        #     if i == m and j == n: return True
        #     if (i, j) in memo: return memo[(i, j)]

        #     k = i + j 
        #     res = (i < m and s1[i] == s3[k] and backtrack(i + 1, j)) or (j < n and s2[j] == s3[k] and backtrack(i, j + 1))

        #     memo[(i, j)] = res

        #     return res

        # return backtrack(0, 0)
        
        