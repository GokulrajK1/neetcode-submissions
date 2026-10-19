class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        m, n = len(s), len(p)

        memo = {}
        
        def backtrack(i, j):

            if (i, j) in memo: return memo[(i, j)]
            if i == m and j == n: return True 
            if i == m and j < n - 1 and p[j + 1] == "*": return backtrack(i, j + 2)
            if i >= m: 
                return False
            if j >= n: 
                return False 

            res = False

            if j + 1 < n and p[j + 1] == "*":
                if s[i] == p[j] or p[j] == ".":    
                   
                    res = res or backtrack(i + 1, j)
                
                res = res or backtrack(i, j + 2)

            else:
                if  s[i] == p[j] or p[j] == ".":
                    res = res or backtrack(i + 1, j + 1)

            memo[(i, j)] = res
            return res

        return backtrack(0, 0)
