class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0: return False 

        n = len(nums)
        target = sum(nums) // 2

        dp = [False] * (target + 1)
        dp[0] = True 

        for i in range(n - 1, -1, -1):
            for a in range(target, 0, -1):
                if a < nums[i]:
                    break
                dp[a] |= dp[a - nums[i]]
                
        return dp[target]


        # memo = {}

        # def backtrack(i, amount):
        #     if (i, amount) in memo: return memo[(i, amount)]
        #     if amount == 0: return True 
        #     if amount < 0: return False 
        #     if i == n: return False

        #     print(i, nums[i], amount)

        #     without_it = backtrack(i + 1, amount)
        #     with_it = backtrack(i + 1, amount - nums[i])

        #     memo[(i, amount)] = without_it or with_it

        #     return without_it or with_it

        # return backtrack(0, target)

