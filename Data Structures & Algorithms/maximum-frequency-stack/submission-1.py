class FreqStack:

    def __init__(self):
        self.stacks = {}
        self.counts = {}
        self.max_count = 0 

    def push(self, val: int) -> None:
        count = self.counts.get(val, 0) + 1 
        self.counts[val] = count
        values = self.stacks.get(count, [])
        values.append(val)
        self.stacks[count] = values 
        self.max_count = max(self.max_count, count)

    def pop(self) -> int:
        value = self.stacks[self.max_count].pop()
        self.counts[value] -= 1 
        if self.stacks[self.max_count] == []:
            self.max_count -= 1 
        return value
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()