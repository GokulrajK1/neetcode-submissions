class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-x for x in nums]
        heapq.heapify(nums)
        count = 0 
        print(nums)
        res = None
        while len(nums) > 0 and count < k:
            count += 1 
            res = heapq.heappop(nums)

        return -res