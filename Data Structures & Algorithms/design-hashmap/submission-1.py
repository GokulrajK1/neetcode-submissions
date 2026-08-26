class ListNode:
    def __init__(self):
        self.key = -1
        self.value = -1
        self.next = None

class MyHashMap:

    def __init__(self):
        self.length = 10 ** 4
        self.dictionary = [ListNode()] * self.length

    def put(self, key: int, value: int) -> None:
        hashed = key % self.length
        curr = self.dictionary[hashed]
        prev = None
        while curr != None:
            if curr.key == key:
                curr.value = value
                return 
            prev = curr
            curr = curr.next 

        prev.next = ListNode()
        prev.next.key = key 
        prev.next.value = value

    def get(self, key: int) -> int:
        hashed = key % self.length
        curr = self.dictionary[hashed]
        while curr != None:
            if curr.key == key:
                return curr.value

            curr = curr.next 

        return -1 

    def remove(self, key: int) -> None:
        hashed = key % self.length
        curr = self.dictionary[hashed]

        if curr != None and curr.key == key:
            self.dicionary[hashed] = curr.next

        prev = None
        while curr != None:
            if curr.key != key:
                prev = curr
                curr = curr.next
                continue 
            
            prev.next = curr.next 
            return 


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)