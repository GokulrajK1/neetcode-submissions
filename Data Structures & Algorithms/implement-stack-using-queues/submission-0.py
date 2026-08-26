class MyStack:

    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, x: int) -> None:
        if self.empty():
            self.queue1.append(x)
        elif self.queue2:
            self.queue1.append(x)
            while self.queue2:
                self.queue1.append(self.queue2.popleft())
        else:
            self.queue2.append(x)
            while self.queue1:
                self.queue2.append(self.queue1.popleft())

    def pop(self) -> int:
        if self.queue1:
            return self.queue1.popleft()
        else:
            return self.queue2.popleft()

    def top(self) -> int:
        if self.queue1:
            return self.queue1[0]
        else:
            return self.queue2[0]


    def empty(self) -> bool:
        return len(self.queue1) == 0 and len(self.queue2) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()