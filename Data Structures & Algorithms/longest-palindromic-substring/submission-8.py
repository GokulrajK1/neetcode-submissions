class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        t = "#" + "#".join(s) + "#"
        m = len(t)
        p = [0] * m 
        l = 0
        r = 0
        for i in range(m):
            p[i] = min(r - i, p[l + (r - i)] if i < r else 0)
            while (i - p[i] - 1) >= 0 and (i + p[i] + 1) < m and t[i - p[i] - 1] == t[i + p[i] + 1]:
                p[i] += 1 

            if i + p[i] > r:
                l = i - p[i]
                r = i + p[i]

        max_length = max(p)
        max_index = p.index(max_length)
        res_index = (max_index - max_length) // 2

        return s[res_index:res_index+max_length]
