class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counts_1 = {}
        ans1 = [0] * 26
        for char in s1:
            counts_1[char] = counts_1.get(char, 0) + 1 
            ans1[ord(char) - ord("a")] = 1 

        counts_2 = {}
        ans2 = [0] * 26 

        i = j = 0
        while j < len(s2):
            if s2[j] not in counts_1:
                j += 1
                counts_2 = {}
                ans2 = [0] * 26 
                continue 
            
            counts_2[s2[j]] = counts_2.get(s2[j], 0) + 1 
            print(counts_2)

            while i < j and counts_2[s2[j]] > counts_1[s2[j]]:
                if s2[i] not in counts_1:
                    i += 1
                    continue 

                counts_2[s2[i]] -= 1 
                if counts_2[s2[i]] != counts_1[s2[i]]:
                    ans2[ord(s2[i]) - ord("a")] = 0 

                i += 1

            if counts_2[s2[j]] == counts_1[s2[j]]:
                ans2[ord(s2[j]) - ord("a")] = 1
                print("hello")

            print(ans2)

            if ans2 == ans1:
                return True 

            j += 1 

        return False 


        