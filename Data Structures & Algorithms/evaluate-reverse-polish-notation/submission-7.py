class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+":
                num2 = stack.pop()
                stack.append(stack.pop() + num2)
            elif token == "-":
                num2 = stack.pop()
                stack.append(stack.pop() - num2)
            elif token == "*":
                num2 = stack.pop()
                stack.append(stack.pop() * num2)
            elif token == "/":
                num2 = stack.pop()
                print(num2)
                stack.append(int(stack.pop() / num2)) 
            else:
                stack.append(int(token))

            print(stack)

        return stack[-1]