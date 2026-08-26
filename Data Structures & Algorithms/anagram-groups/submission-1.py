class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        chars_to_strings = {}
        for string in strs:
            chars = [0] * 26 
            for char in string:
                chars[ord(char) - ord("a")] += 1 
            strings_list = chars_to_strings.get(tuple(chars), [])
            strings_list.append(string)
            chars_to_strings[tuple(chars)] = strings_list
        return list(chars_to_strings.values())
            