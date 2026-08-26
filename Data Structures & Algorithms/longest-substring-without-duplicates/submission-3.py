class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        uniques = set()
        length = 0
        i = 0
        for j in range(len(s)):
            while i < j and s[j] in uniques:
                uniques.remove(s[i])
                i += 1 

            uniques.add(s[j])
            length = max(length, j - i + 1)

        return length

