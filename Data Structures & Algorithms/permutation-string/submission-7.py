class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counts = {}
        for char in s1:
            s1_counts[char] = s1_counts.get(char, 0) + 1
        s2_counts = {}
        left = 0
        for right in range(len(s2)):
            if s2[right] in s1_counts:
                s2_counts[s2[right]] = s2_counts.get(s2[right], 0) + 1 
                if s2_counts == s1_counts:
                    return True 
                while left < right and s2_counts[s2[right]] > s1_counts[s2[right]]:
                    if s2[left] in s2_counts:
                        s2_counts[s2[left]] -= 1 
                    left += 1 
            else:
                left = right
                s2_counts = {}


        return False