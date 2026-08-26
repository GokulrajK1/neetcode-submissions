class ListNode:
    def __init__(self, key, value, next=None):
        self.key = key
        self.value = value 
        self.next = next 

class MyHashMap:

    def __init__(self):
        self.length = 10 ** 4
        self.values = [ListNode(-1, -1)] * self.length 

    def put(self, key: int, value: int) -> None:
        hashed_value = key % self.length 
        head = self.values[hashed_value]
        curr = head
        prev = None 
        while (curr != None):
            if curr.key == key:
                curr.value = value
                return 
            prev = curr
            curr = curr.next

        prev.next = ListNode(key, value)
        

    def get(self, key: int) -> int:
        hashed_value = key % self.length
        head = self.values[hashed_value]
        curr = head 
        while(curr != None):
            if curr.key == key:
                return curr.value
            curr = curr.next

        return -1 

    def remove(self, key: int) -> None:
        hashed_value = key % self.length
        head = self.values[hashed_value]
        curr = head
        prev = None 

        while(curr != None):
            if curr.key == key:
                prev.next = curr.next 
            prev = curr
            curr = curr.next 


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)