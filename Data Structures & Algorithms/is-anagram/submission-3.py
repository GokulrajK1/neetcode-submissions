class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 
        chars = {}

        for i in range(len(s)):
            chars[s[i]] = 1 + chars.get(s[i], 0)
            chars[t[i]] = -1 + chars.get(t[i], 0)

        for c in chars.values():
            if c != 0:
                return False
        return True
        