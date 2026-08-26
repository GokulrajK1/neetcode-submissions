class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counts = [0] * 26
        marked = [0] * 26
        for char in s1:
            counts[ord(char) - ord("a")] += 1 
            marked[ord(char) - ord("a")] = 1 
        left = 0 
        for right in range(len(s2)):
            while left < right and counts[ord(s2[right]) - ord("a")] == 0:
                index = ord(s2[left]) - ord("a")
                if marked[index] == 1:
                    counts[index] += 1
                left += 1
            if counts[ord(s2[right]) - ord("a")] > 0:
                counts[ord(s2[right]) - ord("a")] -= 1 
                print(counts)
                if counts == [0] * 26:
                    return True 

        return False 

