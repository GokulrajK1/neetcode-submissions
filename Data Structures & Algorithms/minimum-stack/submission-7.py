class MinStack:

    def __init__(self):
        self.minimum = float("inf")
        self.stack = []

    def push(self, val: int) -> None:
        if val < self.minimum: 
            self.minimum = val

        self.stack.append((val, self.minimum))

    def pop(self) -> None:
        self.stack.pop()
        self.minimum = float("inf") if not self.stack else self.stack[-1][1]

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        print(self.stack)
        return self.stack[-1][1]
        
