class FreqStack:

    def __init__(self):
        self.stack = {}
        self.counts = {}
        self.max_count = 0

    def push(self, val: int) -> None:
        value_count = self.counts.get(val, 0) + 1 
        self.counts[val] = value_count
        if value_count > self.max_count:
            self.max_count = value_count 
            self.stack[value_count] = []
        self.stack[value_count].append(val)

    def pop(self) -> int:
        res = self.stack[self.max_count].pop()
        self.counts[res] -= 1 
        if self.stack[self.max_count] == []:
            self.max_count -= 1

        return res 


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()