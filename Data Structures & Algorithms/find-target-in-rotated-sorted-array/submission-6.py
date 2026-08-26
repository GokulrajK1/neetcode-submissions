class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums) - 1 
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] == target:
                return mid 
            if nums[lo] > nums[mid]:
                if target >= nums[lo] or target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1 
            else:
                if target >= nums[lo]:
                    if target < nums[mid]:
                        hi = mid - 1
                    else:
                        lo = mid + 1 
                else:
                    lo = mid + 1 

        return -1


        
                
