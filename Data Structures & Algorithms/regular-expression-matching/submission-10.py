class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        def backtrack(i, j):
            if i == m and j == n:
                return True 

            if i == m and j == n - 1 and p[j] == "*":
                return True 

            if i == m and j == n - 2 and p[j + 1] == "*":
                return True 

            if i == m or j == n:
                return False 

            if j < n - 1 and p[j + 1] == "*":
                if s[i] == p[j] or p[j] == ".":
                    if backtrack(i + 1, j):
                        return True 
                return backtrack(i, j + 2)
            else:
                if s[i] == p[j] or p[j] == ".":
                    return backtrack(i + 1, j + 1)
                else:
                    return False 

        return backtrack(0, 0)

            