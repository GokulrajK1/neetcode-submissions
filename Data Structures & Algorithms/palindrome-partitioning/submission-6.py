class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def is_palindrome(i, j):
            while i <= j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1

            return True 

        res = []
        curr = []

        def backtrack(i, length):

            if i == len(s):
                res.append(curr.copy())
                return

            if i + length > len(s):
                return 

            if is_palindrome(i, i + length - 1):
                curr.append(s[i:i+length])
                backtrack(i + length, 1)
                curr.pop()

            backtrack(i, length + 1)


        backtrack(0, 1)

        return res
