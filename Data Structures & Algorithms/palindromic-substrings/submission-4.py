class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        start = 0
        count = 0

        for i in range(len(s)):
            l, r = i, i 
            while l >= 0 and r < n and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1

            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                count += 1 
                l -= 1
                r += 1

        return count
        # t = "#" + "#".join(s) + "#"
        # m = len(t)
        # p = [0] * m 
        # l, r = 0, 0
        # for i in range(m):
        #     p[i] = min(r - i, p[l + (r - i)] if i < r else 0)
        #     left = i - p[i] - 1
        #     right = i + p[i] + 1
        #     while left >= 0 and right < m and t[left] == t[right]:
        #         p[i] += 1
        #         left -= 1
        #         right += 1

        #     if i + p[i] > r:
        #         l = i - p[i]
        #         r = i + p[i]

        # print(p)
        # return sum((x + 1) // 2 for x in p)