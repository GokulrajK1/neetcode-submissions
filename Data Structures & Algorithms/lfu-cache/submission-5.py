class Node:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
        self.use = 1

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

    def is_empty(self):
        return self.first.next == self.last 

class LFUCache:

    def __init__(self, capacity: int):
        self.min_freq = 1
        self.frequencies = {1 : LinkedList()}
        self.cache = {}
        self.capacity = capacity
        self.size = 0 

    def get(self, key: int) -> int:
        if key not in self.cache: return -1
        node = self.cache[key]
        linked_list = self.frequencies[node.use]
        linked_list.delete(node)
        if linked_list.is_empty() and node.use == self.min_freq:
            self.min_freq += 1 
        node.use += 1
        if node.use not in self.frequencies:
            self.frequencies[node.use] = LinkedList()
        self.frequencies[node.use].insert(node)
        return node.value
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            linked_list = self.frequencies[node.use]
            linked_list.delete(node)
            if linked_list.is_empty() and node.use == self.min_freq:
                self.min_freq += 1 
            node.use += 1
            if node.use not in self.frequencies:
                self.frequencies[node.use] = LinkedList()
            self.frequencies[node.use].insert(node)
            return 

        if self.size == self.capacity:
            while self.min_freq not in self.frequencies:
                self.min_freq += 1 
            linked_list = self.frequencies[self.min_freq]
            node = linked_list.first.next
            self.frequencies[self.min_freq].delete(node)
            del self.cache[node.key]
            if linked_list.is_empty():
                self.min_freq += 1 

            self.size -= 1

        self.size += 1 
        node = Node(key, value)
        self.frequencies[1].insert(node)
        self.min_freq = 1
        self.cache[node.key] = node
            
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)