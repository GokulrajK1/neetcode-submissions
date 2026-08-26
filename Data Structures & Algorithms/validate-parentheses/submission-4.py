class Solution:
    def isValid(self, s: str) -> bool:
        matchings = {"{" : "}", "[" : "]", "(" : ")"}
        stack = []
        for char in s:
            if char in matchings.keys():
                stack.append(char)
            elif not stack:
                return False
            elif matchings[stack.pop()] != char:
                return False 

        return len(stack) == 0
