class Solution:
    def maxCoins(self, nums: List[int]) -> int:

        n = len(nums)
        
        def backtrack(l, r, memo):
            if l > r:
                return 0 

            if (l, r) in memo:
                return memo[(l, r)]

            max_value = 0

            for i in range(l, r + 1):
                left, right = 1, 1
                if l > 0: left = nums[l - 1]
                if r < n - 1: right = nums[r + 1]
                burst = left * nums[i] * right 
                rest = backtrack(l, i - 1, memo) + backtrack(i + 1, r, memo)
                recurse = burst + rest
                max_value = max(max_value, recurse)

            memo[(l, r)] = max_value

            return max_value

        return backtrack(0, len(nums) - 1, {})

