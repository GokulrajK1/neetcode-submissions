class MinStack:

    def __init__(self):
        self.stack = []
        self.prefix_min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.prefix_min_stack:
            if val <= self.prefix_min_stack[-1]:
                self.prefix_min_stack.append(val)
        else:
            self.prefix_min_stack.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        if self.prefix_min_stack:
            if val == self.prefix_min_stack[-1]:
                self.prefix_min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.prefix_min_stack[-1]
