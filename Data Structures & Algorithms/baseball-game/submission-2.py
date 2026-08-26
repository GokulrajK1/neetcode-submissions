class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for operation in operations:
            try:
                stack.append(int(operation))
            except:
                if operation == "+":
                    stack.append(stack[-1] + stack[-2])
                elif operation == "D":
                    stack.append(stack[-1] * 2)
                else:
                    stack.pop()

            print(stack)

        return sum(stack)