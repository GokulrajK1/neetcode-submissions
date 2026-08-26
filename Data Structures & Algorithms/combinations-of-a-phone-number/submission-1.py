class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
            
        numbers_to_letters_map = {
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
            if i == len(digits):
                res.append("".join(curr))
                return 

            for char in numbers_to_letters_map[digits[i]]:
                curr.append(char)
                backtrack(i + 1)
                curr.pop()

        backtrack(0)
        return res