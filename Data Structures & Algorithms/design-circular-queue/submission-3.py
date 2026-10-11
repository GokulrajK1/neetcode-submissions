class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k 
        self.queue = [0] * (k + 1)
        self.first = self.last = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False
        self.queue[self.last] = value
        self.last = (self.last + 1) % (self.k + 1)
        return True

    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        value = self.queue[self.first]
        self.first = (self.first + 1) % (self.k + 1)
        return True

    def Front(self) -> int:
        if self.isEmpty(): return -1
        return self.queue[self.first]

    def Rear(self) -> int:
        if self.isEmpty(): return -1
        return self.queue[self.last - 1]

    def isEmpty(self) -> bool:
        return self.first == self.last 

    def isFull(self) -> bool:
        return (self.last + 1) % (self.k + 1) == self.first


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()