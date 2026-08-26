class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matchings = {"(" : ")", "[" : "]", "{" : "}"}
        for char in s:
            if char == "(" or char == "[" or char == "{":
                stack.append(char)
            else:
                if not stack:
                    return False 
                
                if matchings[stack.pop()] != char:
                    return False 

        return not stack  

                