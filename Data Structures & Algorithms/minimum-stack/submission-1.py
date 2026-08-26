class MinStack:

    def __init__(self):
        self.stack = []
        self.prefix_min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        min_val = min(val, self.prefix_min_stack[-1] if self.prefix_min_stack else val)
        self.prefix_min_stack.append(min_val)
    def pop(self) -> None:
        self.stack.pop()
        self.prefix_min_stack.pop()
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.prefix_min_stack[-1]
