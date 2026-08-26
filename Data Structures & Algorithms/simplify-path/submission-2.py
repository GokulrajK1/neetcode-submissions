class Solution:
    def simplifyPath(self, path: str) -> str:
        directories = path.split("/")
        print(directories)
        stack = []
        for directory in directories:
            if directory == "..":
                if stack:
                    stack.pop()
            elif directory == "." or directory == "":
                pass
            else:
                stack.append(directory)

        res = "/" + "/".join(stack)
        return res