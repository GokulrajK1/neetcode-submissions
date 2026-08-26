class Solution:
    def numDecodings(self, s: str) -> int:
        
        n = len(s)

        def backtrack(i, memo):
            nonlocal n
            if i == n:
                return 1

            if int(s[i]) == 0:
                return 0

            if i in memo:
                return memo[i]

            count = backtrack(i + 1, memo)

            if i < n - 1 and (int(s[i:i+2]) >= 10 and int(s[i:i+2]) <= 26):
                count += backtrack(i + 2, memo)
            
            memo[i] = count

            return count 

        return backtrack(0, {})

            