# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0 
        curr = head 
        while curr:
            length += 1 
            curr = curr.next 

        index = length - n 
        prev = None
        curr = head
        for i in range(index):
            prev = curr
            curr = curr.next 

        if curr == head:
            return curr.next

        prev.next = prev.next.next

        return head
        

        

        