class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums) - 1
        res = 0
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] > target:
                hi = mid - 1
            elif nums[mid] < target:
                lo = mid + 1 
                res = lo
            else:
                return mid 

        return res 