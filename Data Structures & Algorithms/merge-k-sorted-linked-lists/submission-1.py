# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists: return None
        return self.merge_sort(0, len(lists) - 1, lists)

    def merge_sort(self, lo, hi, lists):
        if lo >= hi:
            return lists[lo]

        mid = lo + (hi - lo) // 2
        return self.merge(self.merge_sort(lo, mid, lists), self.merge_sort(mid + 1, hi, lists))

    def merge(self, list1, list2):
        dummy = ListNode(-1)
        curr = dummy
        curr1 = list1
        curr2 = list2
        while curr1 or curr2:
            if curr1 and curr2:
                if curr1.val <= curr2.val:
                    curr.next = curr1
                    curr1 = curr1.next
                else:
                    curr.next = curr2
                    curr2 = curr2.next
            elif curr1:
                curr.next = curr1
                curr1 = curr1.next
            else:
                curr.next = curr2
                curr2 = curr2.next

            curr = curr.next 

        return dummy.next