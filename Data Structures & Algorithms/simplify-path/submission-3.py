class Solution:
    def simplifyPath(self, path: str) -> str:
        tokens = path.split("/")
        stack = []
        print(tokens)
        for token in tokens:
            if token == ".":
                pass
            elif token == "..":
                if stack:
                    stack.pop()
            elif token and token != "/":
                 stack.append(token)

            print(stack)


        return "/" + "/".join(stack)