class Node:
    def __init__(self, value, key=None, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next 

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.first = Node(0)
        self.last = Node(0)
        self.first.next = self.last
        self.last.prev = self.first 

    def remove(self, node):
        prev, next = node.prev, node.next 
        prev.next = next 
        next.prev = prev 
        return node 

    def insert(self, node):
        self.last.prev.next = node 
        node.prev = self.last.prev
        node.next = self.last
        self.last.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        else:
            return -1 

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].value = value
            self.remove(self.cache[key])
        else:
            self.cache[key] = Node(value, key=key)
        
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.first.next
            self.remove(lru)
            del self.cache[lru.key]
