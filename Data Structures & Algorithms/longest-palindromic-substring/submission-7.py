class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        res = [-1, -1]
        n = len(s)
        max_length = 0

        for i in range(n):

            l = i
            r = i + 1 
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 > max_length:
                    res = [l, r+1]
                    max_length = r - l + 1
                l -= 1 
                r += 1 

            

            l = i
            r = i
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 > max_length:
                    res = [l, r+1]
                    max_length = r - l + 1
                l -= 1
                r += 1 

            

        return s[res[0]:res[1]]