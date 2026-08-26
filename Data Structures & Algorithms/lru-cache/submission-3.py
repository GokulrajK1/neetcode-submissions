class Node:
    
    def __init__(self, val=-1, prev=None, next=None, key=None):
        self.val = val
        self.prev = prev
        self.next = next 
        self.key = key

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.cache = {}

        self.left, self.right = Node(), Node()
        self.left.next = self.right
        self.right.prev = self.left 

    def insert(self, node):
        self.right.prev.next = node
        node.prev = self.right.prev
        node.next = self.right
        self.right.prev = node 

    def delete(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next
    
    def get(self, key: int) -> int:
        if key not in self.cache: return -1 
        self.delete(self.cache[key])
        self.insert(self.cache[key])
        return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.delete(self.cache[key])
            self.cache[key] = Node(value, key=key)
            self.insert(self.cache[key])
            return 

        if len(self.cache) < self.capacity:
            self.cache[key] = Node(value, key=key)
            self.insert(self.cache[key])
            return

        del self.cache[self.left.next.key]
        self.delete(self.left.next)
        self.cache[key] = Node(value, key=key)
        self.insert(self.cache[key])

        

        


        
