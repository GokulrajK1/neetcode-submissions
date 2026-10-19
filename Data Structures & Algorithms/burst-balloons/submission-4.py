class Solution:
    def maxCoins(self, nums: List[int]) -> int:

        n = len(nums)

        memo = {}
        
        def backtrack(l, r):

            if l > r: return 0

            if (l, r) in memo: return memo[(l, r)]

            max_amount = 0

            for i in range(l, r + 1):
                left = nums[l - 1] if l - 1 >= 0 else 1
                right = nums[r + 1] if r + 1 < n else 1 
                burst = left * nums[i] * right
                total = backtrack(l, i - 1) + burst + backtrack(i + 1, r)
                max_amount = max(max_amount, total)

            memo[(l, r)] = max_amount

            return max_amount

        return backtrack(0, n - 1)

