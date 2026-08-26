# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next 

        
        
        prev = None
        curr = slow.next
        slow.next = None
        while curr:
            tmp = curr.next
            curr.next = prev 
            prev = curr
            curr = tmp 

        
        front, back = head, prev 
        while back:
            tmpFront = front.next
            tmpBack = back.next 
            front.next = back
            back.next = tmpFront 
            front = tmpFront
            back = tmpBack

         

  

        