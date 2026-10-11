# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        i = 1 
        attachLeft = dummy
        attachRight = None 
        curr = head 
        while curr:
            if i < left:
                attachLeft = curr 
            temp = curr
            curr = curr.next 
            if i == right:
                temp.next = None
                attachRight = curr
                break 

            i += 1


        prev = None 
        curr = attachLeft.next 
        attachLeft.next = None
        last = curr 
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp 


        attachLeft.next = prev 
        last.next = attachRight

        return dummy.next

        
