class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first = strs[0]
        for i in range(len(first)):
            for string in strs:
                if i >= len(string) or first[i] != string[i]: 
                    return first[:i]

        return first