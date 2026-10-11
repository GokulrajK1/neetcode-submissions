class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        lo = max(nums)
        hi = sum(nums)
        res = hi
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            count = 0
            total = 0
            for num in nums:
                if total + num > mid:
                    count += 1 
                    total = 0
                total += num

            count += 1 

            if count > k:
                lo = mid + 1
            else:
                res = mid 
                hi = mid - 1

        return res