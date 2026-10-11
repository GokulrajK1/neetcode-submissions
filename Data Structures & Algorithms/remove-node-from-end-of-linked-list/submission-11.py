# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        curr = head
        for i in range(n):
            curr = curr.next

        prev = None
        curr2 = head
        while curr:
            curr = curr.next
            prev = curr2
            curr2 = curr2.next 

        if not prev:
            return curr2.next

        prev.next = curr2.next
        return head