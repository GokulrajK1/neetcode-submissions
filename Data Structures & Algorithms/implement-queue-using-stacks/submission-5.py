class MyQueue:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        old_stack = []
        while self.stack:
            old_stack.append(self.stack.pop())
        self.stack.append(x)
        while old_stack:
            self.stack.append(old_stack.pop())

    def pop(self) -> int:
        return self.stack.pop()

    def peek(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        return len(self.stack) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()