class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        # Top Down

        n = len(s)

        def backtrack(i, memo):
            nonlocal n

            if i == n:
                return True 

            if i in memo:
                return memo[i]

            for j in range(i, n):
                if s[i:j+1] in wordDict:
                    if backtrack(j + 1, memo):
                        memo[i] = True
                        return True
            
            memo[i] = False 
            return False 

        return backtrack(0, {})

                