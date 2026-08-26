class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for string in strs:
            letters = [0] * 26
            for char in string:
                letters[ord(char) - ord('a')] += 1
            t_letters = tuple(letters)
            if t_letters not in groups:
                groups[t_letters] = []
            groups[t_letters].append(string)

        return list(groups.values())