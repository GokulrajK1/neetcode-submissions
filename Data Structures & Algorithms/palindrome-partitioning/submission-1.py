class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        curr = []

        def isPalindrome(string):
            i = 0
            j = len(string) - 1
            while i <= j:
                if string[i] != string[j]:
                    return False

                i += 1
                j -= 1

            return True 


        def backtrack(string):
            nonlocal res, curr
            
            if string == "":
                res.append(curr.copy())
                return 

            for i in range(len(string)):
                substring = string[:i+1]
                if isPalindrome(substring):
                    curr.append(substring)
                    backtrack(string[i+1:])
                    curr.pop()
                
        backtrack(s)
        return res

            