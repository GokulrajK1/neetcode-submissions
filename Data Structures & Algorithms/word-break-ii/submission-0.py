class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        dictionary = set(wordDict)
        res = []
        curr = []
        
        def backtrack(start, end):

            if start == end and end == len(s):
                res.append(" ".join(s[i:j+1] for i, j in curr))
                return

            if end == len(s):
                return
            
            if s[start:end+1] in dictionary:
                curr.append((start, end))
                backtrack(end + 1, end + 1)
                curr.pop()
            
            backtrack(start, end + 1)


        backtrack(0, 0)
        return res 



