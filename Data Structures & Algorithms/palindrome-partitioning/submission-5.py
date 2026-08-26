class Solution:
    def partition(self, s: str) -> List[List[str]]:

        n = len(s)
        curr = []
        res = []

        def isPalindrome(i, j):
            while i <= j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1

            return True 
        
        def backtrack(i, length):
            nonlocal n
            
            if i == n:
                res.append(curr.copy())
                return

            if i + length > n:
                return 

            if isPalindrome(i, i + length - 1):
                curr.append(s[i:i+length])
                backtrack(i + length, 1)
                curr.pop()
                
            backtrack(i, length + 1)

        backtrack(0, 1)
        return res 

            