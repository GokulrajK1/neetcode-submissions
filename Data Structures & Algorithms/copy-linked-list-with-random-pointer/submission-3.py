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
        old_to_copy = {None : None}
        curr = head
        while curr != None:
            old_to_copy[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr != None:
            old_to_copy[curr].next = old_to_copy[curr.next]
            old_to_copy[curr].random = old_to_copy[curr.random]
            curr = curr.next

        return old_to_copy[head]
        # curr = head
        # i = 0
        # index_to_node = {}
        # node_to_index = {}
        # while curr != None:
        #     index_to_node[i] = curr 
        #     node_to_index[curr] = i 
        #     curr = curr.next 
        #     i += 1

        # dummy = new_curr = Node(0)
        
        # prev = None
        # curr = head

        # i = 0

        # index_to_new_node = {}
        # index_to_random_node = {}

        # while curr != None:
        #     new_copy = Node(curr.val)
        #     if prev:
        #         prev.next = new_copy

        #     if i in index_to_random_node:
        #         for node in index_to_random_node[i]:
        #             node.random = new_copy
            
        #     if curr.random == None:
        #         new_copy.random = None 

        #     else:
        #         print(i, node_to_index[curr.random])
        #         if i < node_to_index[curr.random]:
        #             print("hi")
        #             index_to_random_node[node_to_index[curr.random]] = index_to_random_node.get(node_to_index[curr.random], []) + [new_copy]
        #         elif i == node_to_index[curr.random]:
        #             new_copy.random = new_copy
        #         else:
        #             new_copy.random = index_to_new_node[node_to_index[curr.random]]

        #     index_to_new_node[i] = new_copy
        #     new_curr.next = new_copy
        #     new_curr = new_curr.next 

        #     curr = curr.next
        #     i += 1

        # return dummy.next 


