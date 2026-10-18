class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        dp = [0] * (target + 1)
        dp[0] = 1
        for amount in range(1, target + 1):
            for i in range(len(nums)):
                if amount < nums[i]: continue 
                dp[amount] += dp[amount - nums[i]]

        return dp[target]