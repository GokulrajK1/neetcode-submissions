class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        
        def backtrack(opening, closing, curr):
            nonlocal res, n

            if opening == n and closing == n:
                res.append("".join(curr))
                return 

            if opening == n:
                curr.append(")")
                backtrack(opening, closing + 1, curr.copy())

            elif opening == closing:
                curr.append("(")
                backtrack(opening + 1, closing, curr.copy())
            else:
                curr.append("(")
                backtrack(opening + 1, closing, curr.copy())
                curr.pop()
                curr.append(")")
                backtrack(opening, closing + 1, curr.copy())

        backtrack(0, 0, [])
        return res 
