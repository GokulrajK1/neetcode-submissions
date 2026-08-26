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
            if curr1 and curr2:
                tmp = curr1.next 
                total = curr1.val + curr2.val + carry
                if total >= 10:
                    total -= 10
                    carry = 1 
                else:
                    carry = 0
                curr1.val = total
                curr.next = curr1
                curr1 = tmp 
                curr2 = curr2.next 
                print("he")
            elif curr1:
                tmp = curr1.next 
                total = curr1.val + carry
                if total >= 10:
                    total -= 10
                    carry = 1 
                else:
                    carry = 0
                curr1.val = total
                curr.next = curr1
                curr1 = tmp 
            else:
                tmp = curr2.next 
                total = curr2.val + carry
                if total >= 10:
                    total -= 10
                    carry = 1 
                else:
                    carry = 0
                curr2.val = total
                curr.next = curr2
                curr2 = tmp 

            curr = curr.next 
            print(dummy.val)

        if carry == 1:
            curr.next = ListNode(1)

        return dummy.next

