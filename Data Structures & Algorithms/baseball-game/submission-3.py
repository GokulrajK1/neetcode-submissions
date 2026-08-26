class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        total = 0
        for operation in operations:
            try:
                stack.append(int(operation))
            except:
                if operation == "+":
                    stack.append(stack[-1] + stack[-2])
                elif operation == "D":
                    stack.append(stack[-1] * 2)
                else:
                    total -= stack[-1]
                    stack.pop()
                    
                    continue 

            total += stack[-1]

        return total