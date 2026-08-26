class Solution:
    def isPalindrome(self, i, j, s):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1 
            j -= 1
        return True

    def validPalindrome(self, s: str) -> bool:
        i = 0 
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return self.isPalindrome(i, j - 1, s) or self.isPalindrome(i + 1, j, s)
            i += 1 
            j -= 1 

        return True 