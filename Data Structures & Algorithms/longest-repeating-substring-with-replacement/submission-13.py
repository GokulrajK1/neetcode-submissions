class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_count = 0 
        counts = {}
        length = 0
        i = 0
        for j in range(len(s)):
            counts[s[j]] = counts.get(s[j], 0) + 1 
            if counts[s[j]] > max_count: max_count = counts[s[j]]

            while i < j and j - i + 1 > max_count + k:
                counts[s[i]] -= 1
                i += 1

            length = max(length, j - i + 1)

        return length
            