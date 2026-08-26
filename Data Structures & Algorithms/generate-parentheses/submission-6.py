class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        curr = []
        
        def backtrack(opening, closing):
            nonlocal res, n

            if opening == n and closing == n:
                res.append("".join(curr))
                return 

            if opening == n:
                curr.append(")")
                backtrack(opening, closing + 1)
                curr.pop()

            elif opening == closing:
                curr.append("(")
                backtrack(opening + 1, closing)
                curr.pop()
            else:
                curr.append("(")
                backtrack(opening + 1, closing)
                curr.pop()
                curr.append(")")
                backtrack(opening, closing + 1)
                curr.pop()

        backtrack(0, 0)
        return res 
