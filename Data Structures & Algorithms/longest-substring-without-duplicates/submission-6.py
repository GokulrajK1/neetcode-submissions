class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        uniques = set()
        n = len(s)
        length = 0
        i = 0
        for j in range(n):
            while s[j] in uniques:
                uniques.discard(s[i])
                i += 1

            uniques.add(s[j])
            length = max(length, j - i + 1)


        return length