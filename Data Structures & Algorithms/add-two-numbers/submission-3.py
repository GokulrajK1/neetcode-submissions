# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = l1 
        curr2 = l2
        dummy = curr = ListNode()
        carry = 0 
        while curr1 or curr2:
            if curr1 and curr2:
                curr1.val += curr2.val + carry
                carry = 0
                if curr1.val >= 10:
                    carry = 1
                    curr1.val -= 10
                curr.next = curr1
                curr1 = curr1.next
                curr2 = curr2.next
                curr = curr.next
            elif curr1:
                curr1.val += carry
                carry = 0
                if curr1.val >= 10:
                    carry = 1
                    curr1.val -= 10
                curr.next = curr1
                curr1 = curr1.next
                curr = curr.next
            else:
                curr2.val += carry
                carry = 0
                if curr2.val >= 10:
                    carry = 1
                    curr2.val -= 10
                curr.next = curr2
                curr2 = curr2.next
                curr = curr.next

        if carry == 1:
            curr.next = ListNode(1)

        return dummy.next
            
            