import math

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        total = 0 
        left = 0
        min_length = math.inf
        for right in range(len(nums)):
            total += nums[right]
            while left < right and total >= target:
                if right - left + 1 < min_length:
                    min_length = right - left + 1
                total -= nums[left]
                left += 1 
            if total >= target:
                if right - left + 1 < min_length:
                    min_length = right - left + 1
            
            
        return 0 if min_length == math.inf else min_length
    