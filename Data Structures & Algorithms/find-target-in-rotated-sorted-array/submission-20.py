class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo = 0 
        hi = len(nums) - 1 
        while lo <= hi: 
            mid = lo + (hi - lo) // 2 
            print(mid)
            if target < nums[mid]:
                print("less")
                if nums[mid] > nums[hi] and target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
            elif target > nums[mid]:
                print("more")
                if nums[mid] < nums[lo] and target >= nums[lo]:
                    hi = mid - 1
                else:
                    lo = mid + 1

            else:
                return mid

        return -1 