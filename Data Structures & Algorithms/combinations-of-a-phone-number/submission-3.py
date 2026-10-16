class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = {"2" : "abc",
                    "3" : "def",
                    "4" : "ghi",
                    "5" : "jkl",
                    "6" : "mno",
                    "7" : "pqrs",
                    "8" : "tuv",
                    "9" : "wxyz"}

        if digits == "": return []

        res = []
        curr = []

        def backtrack(i):
            if i == len(digits):
                res.append("".join(curr))
                return 

            for letter in letters[digits[i]]:
                curr.append(letter)
                backtrack(i + 1)
                curr.pop()

        backtrack(0)
        return res