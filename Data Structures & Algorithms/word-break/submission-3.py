class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        # Top Down

        # n = len(s)
        
        # wordSet = set(wordDict)
        # t = 0
        # for word in wordDict:
        #     t = max(t, len(word))

        # def backtrack(i, memo):
        #     nonlocal n, t

        #     if i == n:
        #         return True 

        #     if i in memo:
        #         return memo[i]

        #     for j in range(i, i + t + 1):
        #         if s[i:j+1] in wordSet:
        #             if backtrack(j + 1, memo):
        #                 memo[i] = True
        #                 return True
            
        #     memo[i] = False 
        #     return False 

        # return backtrack(0, {})

        # Bottom Up
        n = len(s)
        dp = [False] * (n + 1)
        dp[n] = True 
        for i in range(n - 1, -1, -1):
            for word in wordDict:
                if i + len(word) <= n and s[i:i+len(word)] == word:
                    dp[i] = dp[i+len(word)]
                    if dp[i]:
                        break

        return dp[0]
       

                