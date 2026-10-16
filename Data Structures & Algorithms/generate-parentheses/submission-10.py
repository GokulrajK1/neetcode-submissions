class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        curr = []

        def backtracking(opening, closing):
            if opening == n and closing == n:
                res.append("".join(curr))
                return 
            if opening == n:
                curr.append(")")
                backtracking(opening, closing + 1)
                curr.pop()
            elif opening == closing:
                curr.append("(")
                backtracking(opening + 1, closing)
                curr.pop()
            else:
                curr.append("(")
                backtracking(opening + 1, closing)
                curr.pop()
                curr.append(")")
                backtracking(opening, closing + 1)
                curr.pop()

        backtracking(0, 0)
        return res