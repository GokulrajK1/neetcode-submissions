class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        og_string = strs[0]

        for string in strs[1:]:
            if string.startswith(og_string):
                continue
            else:
                while not string.startswith(og_string):
                    og_string = og_string[:-1]
                    if og_string == "":
                        return ""
        return og_string