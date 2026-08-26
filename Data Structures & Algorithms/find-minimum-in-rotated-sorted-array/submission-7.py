class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo = 0
        hi = len(nums) - 1 
        res = nums[lo]
        while lo <= hi:

            mid = lo + (hi - lo) // 2 

            if nums[mid] >= nums[lo]:
                res = min(res, nums[lo])
                lo = mid + 1 
            else:
                res = min(res, nums[mid])
                hi = mid - 1 

        return res 
