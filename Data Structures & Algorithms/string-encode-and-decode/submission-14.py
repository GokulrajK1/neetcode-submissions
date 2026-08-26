class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            res += f"{len(string)}/{string}?"
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0 
        print(s)
        while i < len(s):
            if s[i] == "?":
                i += 1
                continue
            length = ""
            while s[i] != "/":
                print(s[i])
                length += s[i]
                i += 1
            word = ""
            j = 0
            while j < int(length):
                word += s[i + j + 1]
                j += 1
            i += j + 1
            res.append(word)
            print(res)

        return res

            

