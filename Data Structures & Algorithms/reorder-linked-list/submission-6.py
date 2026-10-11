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
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp 

        dummy = ListNode(-1)
        curr = dummy
        ptr1 = head 
        ptr2 = prev 
        while ptr1 or ptr2:
            if ptr1:
                curr.next = ptr1
                ptr1 = ptr1.next
                curr = curr.next 
            if ptr2:
                curr.next = ptr2
                ptr2 = ptr2.next
                curr = curr.next 

