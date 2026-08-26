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
        # n = len(s)
        # res_index = 0
        # res_length = 0
        # for i in range(n):
        #     a = i
        #     b = i
        #     while (a >= 0 and b < n) and s[a] == s[b]:
        #         if (b - a + 1) > res_length:
        #             res_index = a
        #             res_length = b - a + 1 
        #         a -= 1 
        #         b += 1
            
        #     a = i
        #     b = i + 1
        #     while (a >= 0 and b < n) and s[a] == s[b]:
        #         if (b - a + 1) > res_length:
        #             res_index = a
        #             res_length = b - a + 1  
        #         a -= 1 
        #         b += 1

        # return s[res_index:res_index+res_length]

        # Mancester Algo

        n = len(s)

        def helper():
            t = "#" + "#".join(s) + "#"
            m = len(t)
            p = [0] * m
            l = 0
            r = 0
            for i in range(m):
                p[i] = min(r - i, p[l + (r - i)]) if i < r else 0 
                while (i - p[i] - 1) >= 0 and (i + p[i] + 1) < m and t[i - p[i] - 1] == t[i + p[i] + 1]:
                    p[i] += 1

                if i + p[i] > r:
                    l = i - p[i]
                    r = i + p[i]

            return p 

        res_length, res_middle_index = max((length, index) for index, length in enumerate(helper()))
        res_index = (res_middle_index - res_length) // 2
        return s[res_index:res_index + res_length]


