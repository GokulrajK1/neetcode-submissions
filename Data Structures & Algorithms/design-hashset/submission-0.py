class ListNode:
    def __init__(self, value, next = None):
        self.value = value 
        self.next = next

class MyHashSet:

    def __init__(self):
        self.length = 10 ** 4
        self.values = [ListNode(-1)] * self.length

    def add(self, key: int) -> None:
        hashed = key % self.length 
        linked_list = self.values[hashed]
        while linked_list.next != None:
            if linked_list.value == key:
                return 
            linked_list = linked_list.next 
        if linked_list.value == key:
            return
        linked_list.next = ListNode(key)

    def remove(self, key: int) -> None:
        hashed = key % self.length 
        linked_list = self.values[hashed]
        previous = None
        while linked_list.next != None:
            if linked_list.value == key:
                previous.next = linked_list.next 
                return 
            previous = linked_list 
            linked_list = linked_list.next 

        if linked_list.value == key:
            previous.next = None

    def contains(self, key: int) -> bool:
        hashed = key % self.length 
        linked_list = self.values[hashed]
        while linked_list != None:
            if linked_list.value == key:
                return True 
            linked_list = linked_list.next 
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)