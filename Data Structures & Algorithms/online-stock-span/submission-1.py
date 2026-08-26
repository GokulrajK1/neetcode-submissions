class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        total = 1
        while self.stack and price >= self.stack[-1][0]:
            _, count = self.stack.pop()
            total += count 
        self.stack.append((price, total))
        print(self.stack)
        return total


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)