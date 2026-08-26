# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next 

        if length == 1:
            return

        half = length // 2
        prev = None
        curr = head
        for i in range(half):
            prev = curr
            curr = curr.next 

        if prev:
            prev.next = None

        prev = None 
        while curr:
            tmp = curr.next
            curr.next = prev 
            prev = curr
            curr = tmp 

    
        print(prev)
        curr1, curr2 = head, prev 
        dummy = ListNode(-1)
        while curr1 or curr2:
            if curr1:
                tmp1 = curr1.next
                dummy.next = curr1
                curr1 = tmp1
                dummy = dummy.next

            if curr2:
                tmp2 = curr2.next
                dummy.next = curr2
                curr2 = tmp2
                dummy = dummy.next

        head = dummy.next

  

        