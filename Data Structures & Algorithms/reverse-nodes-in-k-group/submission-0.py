# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = 0 
        prev = None
        dummy = ListNode(-1)
        dummy.next = head
        curr = head
        while curr:
            length += 1
            prev = curr
            curr = curr.next 

        

        if length // k == 0:
            return head 

        reversable_length = (length // k) * k 
        
        prev = None
        curr = dummy
        for i in range(reversable_length + 1):
            tmp = curr.next
            curr.next = prev 
            prev = curr
            curr = tmp 
        
        end = curr
        
        curr = prev
    
        i = 1
        new_end = None
        while curr:
            if i == 1:
                new_end = curr
                
            if i == k or curr.val == -1:
                tmp = curr.next
                
                curr.next = end
                end = new_end
                curr = tmp
                i = 1

            else:
                curr = curr.next
                i += 1

        return dummy.next


