class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        number_letter_map = {
            "2" : ["a", "b", "c"],
            "3" : ["d", "e", "f"],
            "4" : ["g", "h", "i"],
            "5" : ["j", "k", "l"],
            "6" : ["m", "n", "o"],
            "7" : ["p", "q", "r", "s"],
            "8" : ["t", "u", "v"],
            "9" : ["w", "x", "y", "z"]    
        }

        res = []
        curr = []

        def backtrack(i):
            nonlocal res, curr

            if i == len(digits):
                if curr != []:
                    res.append("".join(curr))
                return 

            for letter in number_letter_map[digits[i]]:
                curr.append(letter)
                backtrack(i + 1)
                curr.pop()

        backtrack(0)

        return res
