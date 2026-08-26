# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:   

    def divide(self, lo, hi, lists):
        if lo > hi:
            return None
            
        if lo == hi:
            return lists[lo]
        
        mid = lo + (hi - lo) // 2
        left = self.divide(lo, mid, lists)
        right = self.divide(mid + 1, hi, lists)
        return self.merge(left, right)
         
    def merge(self, left_list, right_list):
        dummy = ListNode(-1)
        curr = dummy
        left = left_list
        right = right_list
        while left or right:
            if left and right:
                if left.val < right.val:
                    curr.next = left 
                    left = left.next 
                else:
                    curr.next = right 
                    right = right.next 
            elif left:
                curr.next = left
                left = left.next 
            else:
                curr.next = right
                right = right.next 

            curr = curr.next 

        return dummy.next 

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        return self.divide(0, len(lists) - 1, lists)


        