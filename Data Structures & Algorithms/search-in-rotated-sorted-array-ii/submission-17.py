class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        lo = 0
        hi = len(nums) - 1
        
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            print(lo, mid, hi)
         
            if nums[mid] == target:
                return True 
            if nums[lo] == nums[mid]:
                lo += 1
                continue
            if nums[lo] > nums[mid]:
                if nums[mid] < target and target <= nums[hi]:
                    lo = mid + 1 
                else:
                    hi = mid - 1
            elif nums[mid] > nums[hi]:
                if target < nums[mid] and target >= nums[lo]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:
                if nums[mid] > target:
                    hi = mid - 1
                else:
                    lo = mid + 1 

        return False