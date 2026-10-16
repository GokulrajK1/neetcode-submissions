class Solution:
    def checkValidString(self, s: str) -> bool:
        p_stack = []
        a_stack = []

        for i, char in enumerate(s):
            if char == "(":
                p_stack.append(i)
            elif char == "*":
                a_stack.append(i)
            else:
                if p_stack:
                    p_stack.pop()
                elif a_stack:
                    a_stack.pop()
                else:
                    return False 

        while p_stack:
            if not a_stack:
                return False

            p = p_stack.pop()
            a = a_stack.pop()

            if p > a:
                return False

        return True
