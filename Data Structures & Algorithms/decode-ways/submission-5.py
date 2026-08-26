class Solution:
    def numDecodings(self, s: str) -> int:
        
        # Top Down DP
        # n = len(s)

        # def backtrack(i, memo):
        #     nonlocal n
        #     if i == n:
        #         return 1

        #     if int(s[i]) == 0:
        #         return 0

        #     if i in memo:
        #         return memo[i]

        #     count = backtrack(i + 1, memo)

        #     if i < n - 1 and (int(s[i:i+2]) >= 10 and int(s[i:i+2]) <= 26):
        #         count += backtrack(i + 2, memo)
            
        #     memo[i] = count

        #     return count 

        # return backtrack(0, {})

        # Bottom up DP
        n = len(s)
        dp = [0] * (n + 1)
        dp[n] = 1 
        for i in range(n - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0 
            else:
                dp[i] = dp[i + 1]

            if i < n - 1 and int(s[i:i+2]) >= 10 and int(s[i:i+2]) <= 26:
                dp[i] += dp[i + 2]

        return dp[0]

            