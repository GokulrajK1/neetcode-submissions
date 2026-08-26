import math

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_counts = {}
        for char in t:
            t_counts[char] = t_counts.get(char, 0) + 1 
        left = 0 
        s_counts = {}
        is_valid = False
        matches = 0  
        min_length = math.inf
        res = ""
        for right in range(len(s)):
            while matches == len(t_counts):
                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    res = s[left:right]
                if s[left] in s_counts:
                    if s_counts[s[left]] - 1 < t_counts[s[left]]:
                        break 
                    s_counts[s[left]] -= 1 
                left += 1 
            if s[right] in t_counts:
                s_counts[s[right]] = s_counts.get(s[right], 0) + 1
                if s_counts[s[right]] == t_counts[s[right]]:
                    matches += 1 

        while matches == len(t_counts):
                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    res = s[left:right+1]
                if s[left] in s_counts:
                    if s_counts[s[left]] - 1 < t_counts[s[left]]:
                        break 
                    s_counts[s[left]] -= 1 
                left += 1 

        return res 
        


