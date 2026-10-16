class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        currMax = 0
        globalMax = nums[0]
        currMin = 0
        globalMin = nums[0]
        total = 0

        for num in nums:
            currMax = max(currMax + num, num)
            globalMax = max(globalMax, currMax)
            currMin = min(currMin + num, num)
            globalMin = min(globalMin, currMin)
            total += num

        return max(globalMax, total - globalMin) if globalMax > 0 else globalMax
            

