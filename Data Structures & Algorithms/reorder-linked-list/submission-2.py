# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr = head
        length = 0 
        while curr:
            length += 1 
            curr = curr.next

        prev = None
        curr = head 
        for i in range(length // 2 + length % 2):
            prev = curr
            curr = curr.next  

        prev.next = None 

        prev = None 
        while curr:
            temp = curr.next 
            curr.next = prev 
            prev = curr 
            curr = temp 

        front = head
        back = prev 

   

        while back:
            temp_front = front.next 
            temp_back = back.next 
            front.next = back 
            back.next = temp_front 
            front = temp_front 
            back = temp_back 

        
            

        
        
        
