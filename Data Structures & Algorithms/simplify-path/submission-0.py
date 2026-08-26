class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        directories = path.split("/")
        for directory in directories:
            if directory == '':
                continue
            if stack and directory == "..":
                stack.pop()
            elif directory == ".":
                continue
            elif directory != "..":
                stack.append(directory)
        
        print(stack)

        return "/" + "/".join(stack)