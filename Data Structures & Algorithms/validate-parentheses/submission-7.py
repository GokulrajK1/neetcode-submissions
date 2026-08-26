class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == "(" or char == "[" or char == "{":
                stack.append(char)
                continue 

            if not stack:
                return False 

            c = stack.pop()
            if (char == ")" and c != "(") or (char == "]" and c != "[") or (char == "}" and c != "{"):
                return False 

        return len(stack) == 0
