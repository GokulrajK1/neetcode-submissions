class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        wd = set(wordDict)

        res = []
        curr = []

        def backtrack(i, length):
            if i == len(s):
                res.append(" ".join(curr))
                return 

            if i + length > len(s): return 

            if s[i:i+length] in wd:
                curr.append(s[i:i+length])
                backtrack(i+length, 1)
                curr.pop()

            backtrack(i, length + 1)

        backtrack(0, 1)

        return res