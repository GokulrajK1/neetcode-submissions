# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head 
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next 

        if prev:
            prev.next = None
        
        prev = None
        while slow != None:
            temp = slow.next 
            slow.next = prev 
            prev = slow
            slow = temp 

        curr = head 
        prev_prev = None

        while prev != None:
            if curr == None:
                prev_prev.next = prev
                break
            temp_curr = curr.next 
            temp_prev = prev.next
            curr.next = prev 
            prev.next = temp_curr
            prev_prev = prev
            prev = temp_prev
            curr = temp_curr


            


    

