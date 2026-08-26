class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        letters_to_strings = {}
        for string in strs:
            letters = [0] * 26 
            for char in string:
                letters[ord(char) - ord("a")] += 1 
            strings = letters_to_strings.get(tuple(letters), [])
            strings.append(string)
            letters_to_strings[tuple(letters)] = strings 

        return list(letters_to_strings.values())
            