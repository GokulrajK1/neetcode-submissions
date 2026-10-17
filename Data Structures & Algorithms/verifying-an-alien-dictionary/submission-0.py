class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        index = {}
        for i, char in enumerate(order):
            index[char] = i 

        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]
            for j in range(len(word1)):
                if j >= len(word2):
                    return False
                if index[word1[j]] > index[word2[j]]:
                    return False
                elif index[word1[j]] < index[word2[j]]:
                    break

        return True