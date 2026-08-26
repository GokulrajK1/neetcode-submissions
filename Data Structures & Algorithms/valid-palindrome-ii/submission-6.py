class Solution:

    def isPalindrome(self, s):
        i = 0
        j = len(s) - 1
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
            if not s[i].isalnum():
                i += 1
                
            elif not s[j].isalnum():
                j -= 1

            elif s[i].lower() == s[j].lower():
                i += 1
                j -= 1

            else:
                return self.isPalindrome(s[i:j]) or self.isPalindrome(s[i+1:j+1])

        return True

            


        return True

             
                