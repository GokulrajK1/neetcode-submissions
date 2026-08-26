class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        
        def backtrack(arr, memo):
            if len(arr) == 0:
                return 0 

            if tuple(arr) in memo:
                return memo[tuple(arr)]

            max_value = 1
            n = len(arr)

            for i in range(n):
                left, right = 1, 1
                if i > 0: left = arr[i - 1]
                if i < n - 1: right = arr[i + 1]
                burst = left * arr[i] * right 
                rest = backtrack(arr[:i] + arr[i+1:], memo)
                recurse = burst + rest
                max_value = max(max_value, recurse)

            memo[tuple(arr)] = max_value

            return max_value

        return backtrack(nums, {})

