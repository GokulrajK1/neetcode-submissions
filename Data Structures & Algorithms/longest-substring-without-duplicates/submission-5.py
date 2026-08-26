class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = j = 0
        n = len(s)
        length = 0
        uniques = set()
        while j < n:
            while i < j and s[j] in uniques:
                uniques.remove(s[i])
                i += 1 

            uniques.add(s[j])
            length = max(length, j - i + 1)
            j += 1 

        return length
        