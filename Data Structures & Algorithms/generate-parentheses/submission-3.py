class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []
        def backtrack(opening, closing):
            if opening == closing == n:
                res.append("".join(stack))
            elif opening == n:
                stack.append(")")
                backtrack(opening, closing + 1)
                stack.pop()
            elif opening == closing:
                stack.append("(")
                backtrack(opening + 1, closing)
                stack.pop()
            else:
                stack.append("(")
                backtrack(opening + 1, closing)
                stack.pop()
                stack.append(")")
                backtrack(opening, closing + 1)
                stack.pop()

        backtrack(0, 0)
        return res