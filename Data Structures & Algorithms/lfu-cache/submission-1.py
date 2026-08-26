class Node:
    def __init__(self, value = -1, prev = None, next = None, key = None):
        self.value = value
        self.prev = prev
        self.next = next 
        self.key = key

class LinkedList:
    def __init__(self):
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

    def isEmpty(self):
        print(self.left == None)
        return self.left.next == self.right and self.right.prev == self.left

    def printList(self):
        curr = self.left
        while curr:
            print(f"Key={curr.key} and Value={curr.value}")
            curr = curr.next 
        
class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.key_to_count = {}
        self.count_to_list = {}
        self.cache = {}
        self.min_count = 1 

    def printCache(self):
        for count, linked_list in self.count_to_list.items():
            print(f"Count={count}, Min_Count={self.min_count}")
            linked_list.printList()
            print("*--")

    def get(self, key: int) -> int:
        print(f"GET(key={key})-----------------------------")
        if key not in self.cache: return -1 
        count = self.key_to_count[key]
        linked_list = self.count_to_list[count]
        linked_list.delete(self.cache[key])
        count += 1 
        self.key_to_count[key] = count
        linked_list = self.count_to_list.get(count, LinkedList())
        linked_list.insert(self.cache[key])
        self.count_to_list[count] = linked_list 
        value = self.cache[key]
        if self.count_to_list[self.min_count].isEmpty():
            self.min_count += 1 
        self.printCache()
        return value.value

    def put(self, key: int, value: int) -> None:
        print(f"PUT (key={key},value={value})-----------------------------")
        if key in self.cache:
            count = self.key_to_count[key]
            linked_list = self.count_to_list[count]
            linked_list.delete(self.cache[key])
            count += 1 
            self.key_to_count[key] = count
            linked_list = self.count_to_list.get(count, LinkedList())
            self.cache[key].value = value
            linked_list.insert(self.cache[key])
            self.count_to_list[count] = linked_list
            print('**')
            print(self.count_to_list[self.min_count].printList())
            print("**")
            if self.count_to_list[self.min_count].isEmpty():
                self.min_count += 1 
            self.printCache()
            return

        if len(self.cache) < self.capacity:
            self.key_to_count[key] = 1
            self.cache[key] = Node(value=value, key=key)
            linked_list = self.count_to_list.get(1, LinkedList())
            linked_list.insert(self.cache[key])
            self.count_to_list[1] = linked_list
            self.min_count = 1
            self.printCache()
            return 

        print(f"Eviction: {self.min_count}")

        linked_list = self.count_to_list[self.min_count]
        to_delete = linked_list.left.next.key
        linked_list.delete(linked_list.left.next)
        del self.cache[to_delete]
        self.key_to_count[key] = 1
        self.cache[key] = Node(value=value, key=key)
        linked_list = self.count_to_list.get(1, LinkedList())
        linked_list.insert(self.cache[key])
        self.count_to_list[1] = linked_list
        self.min_count = 1
        self.printCache()
        
        

        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)