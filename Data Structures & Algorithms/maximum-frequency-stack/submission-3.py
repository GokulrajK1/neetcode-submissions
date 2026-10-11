class FreqStack:

    def __init__(self):
        self.max_freq = 0
        self.counts = {}
        self.stack = []

    def push(self, val: int) -> None:
        freq = self.counts.get(val, 0) + 1 
        if freq > self.max_freq:
            self.max_freq = freq 
            self.stack.append([])

        self.stack[freq - 1].append(val) 
        self.counts[val] = freq 

    def pop(self) -> int:
        value = self.stack[self.max_freq - 1].pop()
        self.counts[value] -= 1 
        if not self.stack[self.max_freq - 1]:
            self.max_freq -= 1

        return value


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()