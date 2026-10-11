class Solution:
    def simplifyPath(self, path: str) -> str:
        tokens = path.split("/")
        stack = []
       
        for token in tokens:
            if not token:
                continue 
            if token == "..":
                if stack:
                    stack.pop()
            elif token != "/" and token != ".":
                 stack.append(token)

        return "/" + "/".join(stack)