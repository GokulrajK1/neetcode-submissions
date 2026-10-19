class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        m, n = len(s), len(t)

        memo = {}
        
        def backtrack(i, j):
            if j == n:
                return 1 
            if i >= m:
                return 0

            if (i, j) in memo: return memo[(i, j)]

            res = 0

            if s[i] == t[j]:
                res += backtrack(i + 1, j + 1)
            
            res += backtrack(i + 1, j)

            memo[(i, j)] = res

            return res

        return backtrack(0, 0) 
