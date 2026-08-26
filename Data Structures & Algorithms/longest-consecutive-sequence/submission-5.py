class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dp = {}
        res = 0 
        for num in nums:
            if num in dp:
                continue

            dp[num] = dp.get(num - 1, 0) + 1 + dp.get(num + 1, 0)
            dp[num - dp.get(num - 1, 0)] = dp[num]
            dp[num + dp.get(num + 1, 0)] = dp[num]
            res = max(res, dp[num])

        return res
            

        