class Solution:
    def numDecodings(self, s: str) -> int:

        memo = {}
        
        def backtrack(i):
            if i in memo:
                return memo[i]
                
            if i == len(s):
                return 1 

            if i > len(s):
                return 0

            if s[i] == "0": 
                return 0

            count = backtrack(i + 1)
            if i < len(s) - 1 and 10 <= int(s[i:i+2]) <= 26:
                count += backtrack(i + 2)

            memo[i] = count 

            return count

        return backtrack(0)
