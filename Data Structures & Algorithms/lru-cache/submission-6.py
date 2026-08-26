class Node:
    def __init__(self, key=None, val=-1, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next 

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left = Node()
        self.right = Node()
        self.left.next = self.right
        self.right.prev = self.left

    def insert(self, node):
        self.right.prev.next = node
        node.prev = self.right.prev 
        node.next = self.right 
        self.right.prev = node 

    def delete(self, node):
        node.prev.next = node.next 
        node.next.prev = node.prev


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self.delete(node)
        self.insert(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value 
            self.delete(node)
            self.insert(node)
             
        elif len(self.cache) < self.capacity:
            node = Node(key, value)
            self.cache[key] = node 
            self.insert(node)

        else:
            print(key, value)
            tmp = self.left.next
            self.delete(self.left.next)
            del self.cache[tmp.key]
            node = Node(key, value)
            self.cache[key] = node 
            self.insert(node)

             

        
