class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        frequencies = {}
        for string in strs:
            counts = [0] * 26
            for char in string:
                counts[ord(char) - ord('a')] += 1 
            strings = frequencies.get(tuple(counts), [])
            strings.append(string)
            frequencies[tuple(counts)] = strings

        return list(frequencies.values())

