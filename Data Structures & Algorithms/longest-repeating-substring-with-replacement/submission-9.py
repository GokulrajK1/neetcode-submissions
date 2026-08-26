class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0] * 26
        i = 0
        j = 0
        n = len(s)
        length = 0
        max_count = 0

        while j < n: 

            count[ord(s[j]) - ord("A")] += 1
            max_count = max(max_count, count[ord(s[j]) - ord("A")])
            
            while i < j and j - i + 1 > max_count + k:
                count[ord(s[i]) - ord("A")] -= 1
                i += 1 

            length = max(length, j - i + 1)
            
            print(length, i, j)
            print(count)
            j += 1

        return length 

            
