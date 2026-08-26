class ListNode:
    def __init__(self):
        self.value = -1
        self.next = None

class MyHashSet:

    def __init__(self):
        self.length = 10 ** 4
        self.dictionary = [ListNode()] * self.length

    def add(self, key: int) -> None:
        hashed = key % self.length
        curr = self.dictionary[hashed]
        prev = None
        while curr != None:
            if curr.value == key:
                return 
            prev = curr
            curr = curr.next 
        prev.next = ListNode()
        prev.next.value = key 

    def remove(self, key: int) -> None:
        hashed = key % self.length
        curr = self.dictionary[hashed]

        if curr != None and curr.value == key:
            self.dicionary[hashed] = curr.next

        prev = None
        while curr != None:
            if curr.value != key:
                prev = curr
                curr = curr.next
                continue 
            
            prev.next = curr.next 
            return 


    def contains(self, key: int) -> bool:
        hashed = key % self.length
        curr = self.dictionary[hashed]
        
        while curr != None:
            if curr.value == key:
                return True

            curr = curr.next 

        return False 


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)