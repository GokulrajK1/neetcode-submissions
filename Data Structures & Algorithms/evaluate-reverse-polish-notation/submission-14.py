class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+":
                num1, num2 = stack.pop(), stack.pop()
                stack.append(num1 + num2)
            elif token == "-":
                num1, num2 = stack.pop(), stack.pop()
                stack.append(-num1 + num2)
            elif token == "*":
                num1, num2 = stack.pop(), stack.pop()
                stack.append(num1 * num2)
            elif token == "/":
                num1, num2 = stack.pop(), stack.pop()
                stack.append(int(1/num1 * num2))
            else:
                stack.append(int(token))

        return stack[0]