class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        n = len(s)
        
        word_dictionary = set(wordDict)

        memo = {}

        def backtrack(i):
            if i in memo: return memo[i]
            if i == n: return True 
            if i > n: return False 

            res = False 

            for j in range(i, n):
                if s[i:j+1] in word_dictionary and backtrack(j+1):
                    res = True
                    break

            memo[i] = res

            return res

        return backtrack(0) 

