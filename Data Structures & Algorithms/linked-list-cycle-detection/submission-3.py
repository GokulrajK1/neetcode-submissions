# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head 

        fast = head 
        while slow:
            slow = slow.next 
      
            fast = fast.next.next if fast and fast.next else None
            print(fast)
            if slow == fast and slow != None:
                return True 
            
        return False