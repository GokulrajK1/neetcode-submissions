class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        og_string = strs[0]

        for string in strs[1:]:
            if og_string in string:
                continue
            else:
                while og_string not in string:
                    og_string = og_string[:-1]
                    if og_string == "":
                        return ""
        return og_string