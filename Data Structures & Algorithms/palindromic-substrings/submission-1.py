class Solution:
    def countSubstrings(self, s: str) -> int:
        # DP solution 
        # n = len(s) 
        # dp = [[False] * n for _ in range(n)]
        # count = 0
        # for i in range(n - 1, -1, -1):
        #     for j in range(i, n):
        #         if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
        #             dp[i][j] = True 
        #             count += 1

        # return count

        # Center Expander 
        n = len(s)
        count = 0
        for i in range(n):
            a = i
            b = i
            while (a >= 0 and b < n) and s[a] == s[b]:
                count += 1
                a -= 1 
                b += 1
            
            a = i
            b = i + 1
            while (a >= 0 and b < n) and s[a] == s[b]:
                count += 1
                a -= 1 
                b += 1

        return count