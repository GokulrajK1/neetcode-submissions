class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counts = {}
        for string in strs:
            count = [0] * 26
            for char in string:
                count[ord(char) - ord('a')] += 1
            tuple_count = tuple(count)
            counts[tuple_count] = counts.get(tuple_count, []) + [string]

        return list(counts.values())
