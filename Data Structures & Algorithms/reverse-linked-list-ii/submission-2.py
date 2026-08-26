# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head 
        before = None
        after = None
        left_node = None
        right_node = None
        prev = dummy
        curr = head
        index = 1 
        while curr:
         
            if index == left:
                before = prev 
                left_node = curr
            if index == right:
                right_node = curr 
                after = curr.next
            if index >= left and index <= right:
                tmp = curr.next
                curr.next = prev 
                prev = curr 
                curr = tmp 
            else:
                prev = curr
                curr = curr.next 

            index += 1

        print(before.val if before else None)
        print(left_node.val)
        print(right_node.val)
        print(after.val if after else None)
        
        before.next = right_node
        left_node.next = after
        return dummy.next



            
                

        
            
