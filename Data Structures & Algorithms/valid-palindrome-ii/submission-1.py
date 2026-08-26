class Solution:
    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        deletion = False 
        while i < j:
            if s[i] != s[j]:
                if s[i] == s[j - 1] and not deletion:
                    i += 1 
                    j -= 2 
                    deletion = True
                elif s[j] == s[i + 1] and not deletion:
                    j -= 1
                    i += 2
                    deletion = True
                else:
                    return False 
            else:
                i += 1
                j -= 1 

        return True 