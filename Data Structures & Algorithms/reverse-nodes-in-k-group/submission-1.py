# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next 
        
        reversable_length = length - length % k
        if reversable_length == 0:
            return head

        dummy = ListNode(-1)
        attached = dummy
        prev = None
        curr = head 
        first = head 
        for i in range(reversable_length + 1):
            if i != 0 and i % k == 0:
                attached.next = prev 
                attached = first 
                first = curr
                prev = None

                if i == reversable_length:
                    attached.next = curr
                    break
           
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp 

        return dummy.next