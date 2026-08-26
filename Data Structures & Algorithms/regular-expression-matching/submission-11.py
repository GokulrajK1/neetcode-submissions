class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        def backtrack(i, j, memo):
            if i == m and j == n:
                return True 

            if i == m and j == n - 1 and p[j] == "*":
                return True 

            if i == m and j == n - 2 and p[j + 1] == "*":
                return True 

            if i == m or j == n:
                return False 

            if (i, j) in memo:
                return memo[(i, j)]

            res = False 

            if j < n - 1 and p[j + 1] == "*":
                if s[i] == p[j] or p[j] == ".":
                    if backtrack(i + 1, j, memo):
                        memo[(i, j)] = True
                        return True
                
                res = backtrack(i, j + 2, memo)
            else:
                if s[i] == p[j] or p[j] == ".":
                    res = backtrack(i + 1, j + 1, memo)

            memo[(i, j)] = res

            return res 

        return backtrack(0, 0, {})

            