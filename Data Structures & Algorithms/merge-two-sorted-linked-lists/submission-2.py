# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = curr = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next 

            curr = curr.next
                
        
        curr.next = list1 or list2 
        return head.next
        # curr1 = list1 
        # prev1 = None
        # curr2 = list2 
        # while curr2 != None:
        #     if curr1 == None:
        #         if prev1 == None:
        #             prev1 = curr2
        #             list1 = prev1
        #             curr2 = curr2.next
        #             continue
        #         prev1.next = curr2
        #         prev1 = prev1.next
        #         curr2 = curr2.next
        #     elif curr2.val < curr1.val:
        #         temp2 = curr2 
        #         curr2 = curr2.next 
        #         if prev1:
        #             prev1.next = temp2 
        #         else:
        #             list1 = temp2
        #         temp2.next = curr1
        #         curr1 = temp2 
        #     else:
        #         prev1 = curr1 
        #         curr1 = curr1.next 

        # return list1
                     