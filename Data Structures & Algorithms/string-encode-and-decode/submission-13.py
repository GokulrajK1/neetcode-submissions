class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            res += str(len(string)) + "#" + string 

        return res 

    def decode(self, s: str) -> List[str]:

        # print(s)

        strings = []
        i = j = 0 
        while i < len(s):
            
            while j < len(s) and s[j] != "#":
                j += 1 

            # print(i, j)

            length = int(s[i:j])
            end = j + 1 + length
            strings.append(s[j+1:end])
            i = j = end 

        return strings
            
