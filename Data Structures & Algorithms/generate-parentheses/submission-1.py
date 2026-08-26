class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(string, opening, closing):
            if opening == closing == n:
                res.append(string)
                return 
            if opening == n:
                backtrack(string + ")", opening, closing + 1)
            elif opening == closing:
                backtrack(string + "(", opening + 1, closing)
            else:
                backtrack(string + "(", opening + 1, closing)
                backtrack(string + ")", opening, closing + 1)

        backtrack("(", 1, 0)
        return res 


            
            