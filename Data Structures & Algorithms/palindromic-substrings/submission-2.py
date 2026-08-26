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
        # n = len(s)
        # count = 0
        # for i in range(n):
        #     a = i
        #     b = i
        #     while (a >= 0 and b < n) and s[a] == s[b]:
        #         count += 1
        #         a -= 1 
        #         b += 1
            
        #     a = i
        #     b = i + 1
        #     while (a >= 0 and b < n) and s[a] == s[b]:
        #         count += 1
        #         a -= 1 
        #         b += 1

        # return count

        #Mancester
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

        p = helper()
        res = 0 
        for length in p:
            res += (length + 1) // 2

        return res

        