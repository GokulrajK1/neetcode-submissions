class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counts1 = {}
        for char in s1:
            counts1[char] = counts1.get(char, 0) + 1 

        counts2 = {}
        i = 0 
        for j in range(len(s2)):
            if s2[j] not in counts1:
                counts2 = {}
                i = j + 1 
                continue 

            counts2[s2[j]] = counts2.get(s2[j], 0) + 1 
            while i < j and counts2[s2[j]] > counts1[s2[j]]:
                counts2[s2[i]] -= 1
                i += 1 

            if counts2 == counts1: return True

        return False 


        