class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        n = len(s)
        
        word_dictionary = set(wordDict)

        # memo = {}

        # def backtrack(i):
        #     if i in memo: return memo[i]
        #     if i == n: return True 
        #     if i > n: return False 

        #     res = False 

        #     for j in range(i, n):
        #         if s[i:j+1] in word_dictionary and backtrack(j+1):
        #             res = True
        #             break

        #     memo[i] = res

        #     return res

        # return backtrack(0) 

        dp = [False] * (n + 1)
        dp[n] = True
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i:j+1] in word_dictionary:
                    dp[i] |= dp[j+1]
        
        return dp[0]

