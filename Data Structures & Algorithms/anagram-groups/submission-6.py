class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        frequencies = defaultdict(list)
        for string in strs:
            chars = [0] * 26
            for char in string:
                chars[ord(char) - ord("a")] += 1

            frequencies[tuple(chars)].append(string)

        return list(frequencies.values())