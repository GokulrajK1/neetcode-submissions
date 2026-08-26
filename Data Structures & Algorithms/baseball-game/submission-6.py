class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        total = 0
        for operation in operations:
            if operation == "+":
                x = stack[-1] + stack[-2]
                total += x 
                stack.append(x)
            elif operation == "C":
                total -= stack.pop()
            elif operation == "D":
                x = stack[-1] * 2
                total += x 
                stack.append(x)
            else:
                stack.append(int(operation))
                total += int(operation)
            print(stack, total)

        return total 