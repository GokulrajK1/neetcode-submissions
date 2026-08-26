"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return None 

        dummy = Node(0)
        ptr = head
        curr = dummy 
        storage = {}
        while ptr:
            curr.next = Node(ptr.val, ptr.next, ptr.random)
            storage[ptr] = curr.next 
            ptr = ptr.next 
            curr = curr.next 

        new_head = dummy.next
        curr = new_head
        while curr:
            if curr.random:
                curr.random = storage[curr.random]
            curr = curr.next 

        return new_head


     
