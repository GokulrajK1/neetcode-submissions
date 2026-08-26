# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr1 = head 
        for i in range(n):
            if not curr1:
                break
            curr1 = curr1.next 

        prev = None 
        curr2 = head 
        while curr1:
            prev = curr2 
            curr2 = curr2.next
            curr1 = curr1.next 

        if prev == None: 
            return head.next 

        prev.next = curr2.next 
        return head
            

        