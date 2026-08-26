# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        fast = head
        count = 0 
        while fast != None and fast.next != None:
            count += 1 
            fast = fast.next.next
        
        if fast == None:
            length = count * 2 
        elif fast.next == None:
            length = count * 2 + 1 


        prev = None
        curr = head

        for i in range(length - n):
            prev = curr 
            curr = curr.next

        if n == length:
            return head.next

        if prev:
            prev.next = curr.next

        return head



