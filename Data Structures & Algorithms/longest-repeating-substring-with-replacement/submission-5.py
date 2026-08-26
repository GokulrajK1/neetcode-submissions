class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_count = 0 
        left = 0 
        counts = {}
        max_length = 0 
        for right in range(len(s)):
            counts[s[right]] = counts.get(s[right], 0) + 1 
            if counts[s[right]] > max_count:
                max_count = counts[s[right]]
            while right - left + 1 > max_count + k:
                counts[s[left]] -= 1 
                left += 1 
            if right - left + 1 > max_length:
                max_length = right - left + 1 

        return max_length 
            