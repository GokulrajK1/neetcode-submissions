class ListNode:

    def __init__(self, val = -1, prev = None, next = None):
        self.val = val
        self.prev = prev
        self.next = next

class MyCircularQueue:

    def __init__(self, k: int):
        self.front = ListNode()
        curr = self.front 

        for i in range(k - 1):
            curr.next = ListNode()
            curr.next.prev = curr
            curr = curr.next 

        self.back = curr
        self.back.next = self.front 
        self.front.prev = self.back 
        self.curr = self.front 

    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False 

        self.curr.val = value 
        self.curr = self.curr.next 
        return True

    def deQueue(self) -> bool:
        if self.isEmpty(): return False 

        self.front.val = -1
        self.front = self.front.next 
       
        self.back = self.front.prev 
        return True

    def Front(self) -> int:
        return self.front.val

    def Rear(self) -> int:
        return self.curr.prev.val

    def isEmpty(self) -> bool:
        return self.front.val == -1 
        
    def isFull(self) -> bool:
        return self.back.val != -1 
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()