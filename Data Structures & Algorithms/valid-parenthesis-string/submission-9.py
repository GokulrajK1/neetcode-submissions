class Solution:
    def checkValidString(self, s: str) -> bool:
        pStack, sStack = [], []
        for i, char in enumerate(s):
            if char == "(":
                pStack.append(i)
            elif char == "*":
                sStack.append(i)
            else:
                if pStack:
                    pStack.pop()
                elif sStack:
                    sStack.pop()
                else:
                    return False 

        while pStack and sStack:
            x, y = pStack.pop(), sStack.pop()
            if y <= x:
                return False

        return len(pStack) == 0



