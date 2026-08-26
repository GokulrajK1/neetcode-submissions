class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo = 0 
        hi = len(nums) - 1 
        res = nums[0]
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if nums[lo] > nums[mid]:
                res = min(res, nums[mid])
                hi = mid - 1 
            elif nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                res = min(res, nums[lo])
                hi = mid - 1 

        return res
