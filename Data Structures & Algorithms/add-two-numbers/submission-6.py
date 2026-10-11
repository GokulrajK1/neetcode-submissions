# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        curr1 = l1
        curr2 = l2
        dummy = ListNode(-1)
        curr = dummy
        while curr1 or curr2:
            v1 = curr1.val if curr1 else 0
            v2 = curr2.val if curr2 else 0
            value = v1 + v2 + carry 
            curr.next = ListNode(value % 10)
            carry = 1 if value >= 10 else 0
            curr = curr.next 
            curr1 = curr1.next if curr1 else None
            curr2 = curr2.next if curr2 else None

        if carry == 1:
            curr.next = ListNode(1)

        return dummy.next
