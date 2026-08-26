class Solution:
    def longestPalindrome(self, s: str) -> str:
        res_idx, res_length = 0, 0 
        memo = [[False] * len(s) for _ in range(len(s))]
        for i in range(len(s) - 1, -1, -1):
            for j in range(len(s)):
                if s[i] == s[j] and (j - i <= 2 or memo[i + 1][j -1]):
                    memo[i][j] = True
                    if res_length < (j - i + 1):
                        res_idx = i
                        res_length = j - i + 1

        return s[res_idx : res_idx + res_length]