class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            res += f"{len(string)}:{string}"

        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while j < len(s) and s[j] != ":":
                j += 1

            length = s[i:j]
            res.append(s[j+1:j+1+int(length)])
            i = j+1+int(length)

        return res
        

