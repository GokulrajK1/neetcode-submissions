class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        dp = defaultdict(int)
        dp[0] = 1

        n = len(nums)

        for i in range(n):
            copy_dp = defaultdict(int)
            for amount in dp:
                copy_dp[amount + nums[i]] += dp[amount]
                copy_dp[amount - nums[i]] += dp[amount]

            dp = copy_dp
            
        return dp[target]