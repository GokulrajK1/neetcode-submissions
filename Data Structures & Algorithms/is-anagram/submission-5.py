class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 

        chars_list = [0] * 26
        for i in range(len(s)):
            chars_list[ord(s[i]) - ord("a")] += 1 
            chars_list[ord(t[i]) - ord("a")] -= 1 

        return chars_list == [0] * 26
