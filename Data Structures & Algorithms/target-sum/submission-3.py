class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # Top Down
        n = len(nums)
        def backtrack(i, remaining, memo):
            if (i, remaining) in memo:
                return memo[(i, remaining)]

            if remaining == target and i == n: 
                return 1 

            if i == n:
                return 0 

            memo[(i + 1, remaining + nums[i])] = backtrack(i + 1, remaining + nums[i], memo) 
            memo[(i + 1, remaining - nums[i])] = backtrack(i + 1, remaining - nums[i], memo)
            return memo[(i + 1, remaining + nums[i])] + memo[(i + 1, remaining - nums[i])]

        return backtrack(0, 0, {})