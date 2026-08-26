# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        curr = dummy
        curr1, curr2 = l1, l2
        carry = 0 
        while curr1 or curr2:
            curr1_val = 0 
            curr2_val = 0
            if curr1 and curr2:
                curr1_val = curr1.val
                curr2_val = curr2.val 
                curr1 = curr1.next
                curr2 = curr2.next
            elif curr1:
                curr1_val = curr1.val
                curr1 = curr1.next
            else:
                curr2_val = curr2.val
                curr2 = curr2.next

            value = curr1_val + curr2_val + carry
            if value >= 10:
                value -= 10 
                carry = 1
            else:
                carry = 0 
            
            curr.next = ListNode(value)
            curr = curr.next 

        if curr == dummy:
            return ListNode() 

        if carry == 1:
            curr.next = ListNode(1)

        return dummy.next