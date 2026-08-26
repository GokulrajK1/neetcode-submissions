class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            res += f"{len(string)}/{string}"
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0 
        while i < len(s):
            length = ""
            while s[i] != "/":
                length += s[i]
                i += 1
            word = ""
            j = i + 1
            while j < len(s) and j < i + 1 + int(length):
                word += s[j]
                j += 1
            i = j 
            res.append(word)
            print(res)

        return res

            

