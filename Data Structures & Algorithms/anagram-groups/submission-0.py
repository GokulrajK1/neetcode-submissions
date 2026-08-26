class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sublists = defaultdict(list)
        for string in strs:
            chars = [0] * 26 
            for char in string:
                chars[ord(char) - ord("a")] += 1 
            sublists[tuple(chars)].append(string)

        return sublists.values()
            