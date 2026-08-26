class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        self.stack.append((price, 1))
        while len(self.stack) > 1 and self.stack[-2][0] <= self.stack[-1][0]:
            s1, s2 = self.stack.pop(), self.stack.pop()
            self.stack.append((s1[0], s1[1] + s2[1]))
        return self.stack[-1][1]





        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)