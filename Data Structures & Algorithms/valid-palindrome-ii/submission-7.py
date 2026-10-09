class Solution:

    def isPalindrome(self, s : str):
        i = 0 
        j = len(s) - 1
        while i <= j:
            if s[i] != s[j]:
                return False

            i += 1 
            j -= 1

        return True 

    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i <= j:
            if s[i] != s[j]:
                return self.isPalindrome(s[i+1:j+1]) or self.isPalindrome(s[i:j])

            i += 1
            j -= 1

        return True