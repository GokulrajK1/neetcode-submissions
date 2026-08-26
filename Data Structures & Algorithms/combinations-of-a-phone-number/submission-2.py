class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if digits == "":
            return []
        digits_to_chars = {
            2 : "abc",
            3 : "def",
            4 : "ghi",
            5 : "jkl",
            6 : "mno",
            7 : "pqrs",
            8 : "tuv",
            9 : "wxyz"
        }

        res = []
        curr = []
        n = len(digits)

        def backtrack(i):
            nonlocal n 
            
            if i == n:
                res.append("".join(curr))
                return 

            for char in digits_to_chars[int(digits[i])]:
                curr.append(char)
                backtrack(i + 1)
                curr.pop()

        backtrack(0)
        return res 
