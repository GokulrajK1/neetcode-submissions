class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_total = nums[0]
        total = 0
        for num in nums:
            if total < 0:
                total = 0

            total += num 
            max_total = max(max_total, total)

        return max_total 