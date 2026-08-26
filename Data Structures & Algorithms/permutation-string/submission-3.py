class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # counts = [0] * 26
        # marked = [0] * 26
        # for char in s1:
        #     counts[ord(char) - ord("a")] += 1 
        #     marked[ord(char) - ord("a")] = 1 
        # left = 0 
        # for right in range(len(s2)):
        #     while left < right and counts[ord(s2[right]) - ord("a")] == 0:
        #         index = ord(s2[left]) - ord("a")
        #         if marked[index] == 1:
        #             counts[index] += 1
        #         left += 1
        #     if counts[ord(s2[right]) - ord("a")] > 0:
        #         counts[ord(s2[right]) - ord("a")] -= 1 
        #         print(counts)
        #         if counts == [0] * 26:
        #             return True 

        # return False 

        s1_counts = {}
        for char in s1:
            s1_counts[char] = s1_counts.get(char, 0) + 1 
        print(s1_counts)
        s2_counts = {}
        left = 0
        for right in range(len(s2)):
            if right - left + 1 > len(s1):
                print("hey")
                print(s2_counts)
                if s2[left] in s2_counts:
                    s2_counts[s2[left]] -= 1 
                left += 1
        
            if s2[right] in s1_counts:
                s2_counts[s2[right]] = s2_counts.get(s2[right], 0) + 1
                if s2_counts == s1_counts:
                    return True

        return False
        

