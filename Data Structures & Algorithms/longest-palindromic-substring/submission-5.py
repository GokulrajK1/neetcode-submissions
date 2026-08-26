class Solution:
    def longestPalindrome(self, s: str) -> str:
        # DP solution 
        # n = len(s) 
        # dp = [[False] * n for _ in range(n)]
        # res_index = 0
        # res_length = 0 
        # for i in range(n - 1, -1, -1):
        #     for j in range(i, n):
        #         if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
        #             dp[i][j] = True 
        #             if j - i + 1 > res_length:
        #                 res_length = max(res_length, j - i + 1)
        #                 res_index = i

        # return s[res_index:res_index + res_length]

        # Center Expander 
        n = len(s)
        res_index = 0
        res_length = 0
        for i in range(n):
            a = i
            b = i
            while (a >= 0 and b < n) and s[a] == s[b]:
                if (b - a + 1) > res_length:
                    res_index = a
                    res_length = b - a + 1 
                a -= 1 
                b += 1
            
            a = i
            b = i + 1
            while (a >= 0 and b < n) and s[a] == s[b]:
                if (b - a + 1) > res_length:
                    res_index = a
                    res_length = b - a + 1  
                a -= 1 
                b += 1

        return s[res_index:res_index+res_length]


