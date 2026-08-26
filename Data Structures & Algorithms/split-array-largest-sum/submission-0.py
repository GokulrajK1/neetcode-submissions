class Solution:
    def check_sum(self, nums, mid, k):
        total = 0 
        count = 1
        for num in nums:
            if total + num > mid: 
                 count += 1 
                 total = 0
            total += num

        print("Count", count)

        if count > k:
            return False
        return True
        
    def splitArray(self, nums: List[int], k: int) -> int:
        lo = max(nums)
        hi = sum(nums)
        print(lo, hi)
        res = hi
        while lo <= hi: 
            mid = lo + (hi - lo) // 2 
            print(mid)
            if self.check_sum(nums, mid, k):
                res = min(res, mid)
                hi = mid - 1
            else:
                lo = mid + 1

        return res

