class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        wd = set(wordDict)

        memo = {}

        def backtrack(i, length):
            if i == len(s):
                return [""]

            if (i, length) in memo: return memo[(i, length)]

            if i + length > len(s): return []

            output = []
            word = s[i:i+length]

            if s[i:i+length] in wd:
                for rest in backtrack(i+length, 1):
                    output.append(word + " " + rest if rest else word)
        

            output += backtrack(i, length + 1)

            memo[(i, length)] = output

            return output

        return backtrack(0, 1)
