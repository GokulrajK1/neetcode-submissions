class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        m, n = len(s), len(p)

        memo = {}
        
        def backtrack(i, j):

            if (i, j) in memo: return memo[(i, j)]

            if j == n:
                return i == m

            res = False

            first = i < m and (s[i] == p[j] or p[j] == ".")
            if j < n - 1 and p[j + 1] == "*":
                res = backtrack(i, j + 2) or (first and backtrack(i + 1, j))
            else:
                res = first and backtrack(i + 1, j + 1)

            memo[(i, j)] = res

            return res

        return backtrack(0, 0)


