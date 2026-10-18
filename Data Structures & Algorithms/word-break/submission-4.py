class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        n = len(s)
        
        word_dictionary = set(wordDict)

        memo = {}

        def backtrack(i, length):
            if i in memo: return memo[i]
            if i == n: return True 
            if i + length > n: return False 

            next_word = s[i:i+length] in wordDict and backtrack(i+length, 1)
            extend = backtrack(i, length + 1)

            memo[i] = next_word or extend

            return next_word or extend

        return backtrack(0, 0) 

