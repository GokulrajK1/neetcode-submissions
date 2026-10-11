class Node:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.first = Node(-1)
        self.last = Node(-1)
        self.first.next = self.last
        self.last.prev = self.first

    def insert(self, node):
        prev = self.last.prev 
        prev.next = node
        node.prev = prev
        node.next = self.last
        self.last.prev = node 

    def delete(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev 

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.size = 0 
        self.linked_list = LinkedList()

    def get(self, key: int) -> int:
        if key not in self.cache: return -1 
        node = self.cache[key]
        self.linked_list.delete(node)
        self.linked_list.insert(node)
        return node.value
        

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            node = self.cache[key]
            node.value = value 
            self.linked_list.delete(node)
            self.linked_list.insert(node)
            return 

        if self.size == self.capacity:
            node = self.linked_list.first.next
            self.linked_list.delete(node)
            del self.cache[node.key]
            self.size -= 1 

        self.size += 1
        node = Node(key, value)
        self.cache[node.key] = node
        self.linked_list.insert(node)

        


        
