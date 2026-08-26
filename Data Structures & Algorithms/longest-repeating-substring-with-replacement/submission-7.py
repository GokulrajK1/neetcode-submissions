class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = [0] * 26 
        i = 0 
        max_length = 0
        max_count = 0 
        for j in range(len(s)):

            counts[ord(s[j]) - ord("A")] += 1 
            if max_count < counts[ord(s[j]) - ord("A")]:
                max_count = counts[ord(s[j]) - ord("A")]

            while j - i + 1 > max_count + k:
             
                counts[ord(s[i]) - ord("A")] -= 1 
                i += 1 

            
            max_length = max(max_length, j - i + 1)

        return max_length