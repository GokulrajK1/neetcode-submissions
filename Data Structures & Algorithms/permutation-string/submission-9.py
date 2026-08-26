class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counts = {}
        for char in s1:
            s1_counts[char] = s1_counts.get(char, 0) + 1

        start = -1
        for i in range(len(s2)):
            if s2[i] in s1_counts:
                start = i 
                break 

        if start == -1:
            return False 

        s2_counts = {}
        i = start 
        for j in range(start, len(s2)):
            s2_counts[s2[j]] = s2_counts.get(s2[j], 0) + 1 
            while i < j and (s2[j] not in s1_counts or s2_counts[s2[j]] > s1_counts[s2[j]]):
                s2_counts[s2[i]] -= 1 
                i += 1 
            
            flag = True
            for char, count in s1_counts.items():
                if char not in s2_counts or s2_counts[char] != s1_counts[char]:
                    flag = False

            if flag:
                return True

            print(s2_counts)

        return False
