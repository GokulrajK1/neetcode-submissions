import math

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        total = 0
        res = math.inf
        for right in range(len(nums)):
            total += nums[right]
            while left < right and total >= target:
                res = min(right - left + 1, res)
                total -= nums[left]
                left += 1 
            if total >= target:
                res = min(right - left + 1, res)
                
        if res == math.inf:
            return 0
        return res
        

            
