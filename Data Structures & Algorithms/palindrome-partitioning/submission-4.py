class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        curr = []

        def isPalindrome(i, j):
            while i <= j:
                if s[i] != s[j]:
                    return False

                i += 1
                j -= 1

            return True 

        def backtrack(i):
            if i == len(s):
                res.append(curr.copy())

            for j in range(i, len(s)):
                if not isPalindrome(i, j):
                    continue

                curr.append(s[i:j+1])
                backtrack(j + 1)
                curr.pop()

        backtrack(0)
        return res 