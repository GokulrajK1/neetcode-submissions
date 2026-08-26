class FreqStack:

    def __init__(self):
        self.max_count = 0
        self.counts = {}
        self.stack = []

    def push(self, val: int) -> None:
        count = self.counts.get(val, 0) + 1 
        self.counts[val] = count
        if count > self.max_count:
            self.max_count = count 
            self.stack.append([val])
        else:
            self.stack[count - 1].append(val)

    def pop(self) -> int:
        val = self.stack[self.max_count - 1].pop()
        self.counts[val] -= 1 
        if self.stack[self.max_count - 1] == []:
            self.max_count -= 1 
            self.stack.pop()
        return val


        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()