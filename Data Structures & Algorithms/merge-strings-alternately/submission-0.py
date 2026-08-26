class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        i = 0 
        j = 0 
        length1 = len(word1)
        length2 = len(word2)
        while True:
            if i < length1 and j < length2:
                result += word1[i] + word2[j]
                i += 1 
                j += 1 
            elif i < length1:
                result += word1[i]
                i += 1 
            elif j < length2:
                result += word2[j]
                j += 1 
            else:
                break 

        return result 

            