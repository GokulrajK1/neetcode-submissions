class Solution:
    def partition(self, s: str) -> List[List[str]]:


        dp = [[False] * len(s) for _ in range(len(s))]
        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if j < i: continue 
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True

        res = []
        curr = []

        def backtrack(i, length):

            if i == len(s):
                res.append(curr.copy())
                return

            if i + length > len(s):
                return 

            if dp[i][i + length - 1]:
                curr.append(s[i:i+length])
                backtrack(i + length, 1)
                curr.pop()

            backtrack(i, length + 1)


        backtrack(0, 1)

        return res
