class Solution:
    def numDecodings(self, s: str) -> int:

        n = len(s)
        
        def backtrack(i, memo):
            nonlocal n

            if i in memo:
                return memo[i]

            if i == n:
                return 1 

            if s[i] == "0":
                return 0 

            one = 0
            num = int(s[i])
            if num >= 1 and num <= 9:
                one = backtrack(i + 1, memo)

            two = 0
            if i < n - 1:
                num = int(s[i:i+2])
                if num >= 10 and num <= 26:
                    two = backtrack(i + 2, memo)

            memo[i] = one + two

            return one + two

        return backtrack(0, {})

            