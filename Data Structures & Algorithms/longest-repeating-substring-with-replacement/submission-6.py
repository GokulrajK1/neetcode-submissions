class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = [0] * 26 
        i = 0 
        max_length = 0
        max_count_letter = 0
        for j in range(len(s)):

            print(counts)

            counts[ord(s[j]) - ord("A")] += 1 
            if counts[max_count_letter] < counts[ord(s[j]) - ord("A")]:
                max_count_letter = ord(s[j]) - ord("A")

            
            while j - i + 1 > counts[max_count_letter] + k:
                print(max_count_letter)
                counts[ord(s[i]) - ord("A")] -= 1 
                i += 1 

                for l in range(26):
                    if counts[l] > counts[max_count_letter]:
                        max_count_letter = l

            
            max_length = max(max_length, j - i + 1)

        return max_length