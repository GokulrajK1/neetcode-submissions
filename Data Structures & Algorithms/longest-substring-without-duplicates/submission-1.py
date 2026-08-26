class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0 
        max_length = 0 
        length = 0
        seen = set()
        for r in range(len(s)):
            if s[r] in seen:
                if length > max_length:
                    max_length = length 
                while s[r] in seen:
                    seen.remove(s[l])
                    l += 1 
                    length -= 1
         
            seen.add(s[r])
            length += 1 

        if length > max_length:
            max_length = length

        return max_length