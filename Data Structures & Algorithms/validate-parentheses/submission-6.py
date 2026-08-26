class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == "(" or c == "[" or c == "{":
                stack.append(c)
                continue
       
            if stack:
                matching = stack.pop()
            
                if (c == ")" and matching != "(") or (c == "]" and matching != "[") or (c == "}" and matching != "{"):
                    return False 
            else:
                return False

       

        return True if not stack else False

