class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) < 2:
            return nums[0]

        memo = {0 : nums[0], 1 : max(nums[0], nums[1])}

        for i in range(2, len(nums)):
            memo[i] = max(memo[i -1], nums[i] + memo[i - 2])

        return memo[len(nums) - 1]
