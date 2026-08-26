class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        n = len(nums)
        if total % 2 != 0: return False 
        amount = total // 2
        
        # def backtrack(i, curr, memo):

        #     if (i, curr) in memo:
        #         return memo[(i, curr)]

        #     if curr == amount:
        #         return True

        #     if curr > amount:
        #         return False 

        #     if i == n:
        #         return False 

        #     included = backtrack(i + 1, curr + nums[i], memo) 
        #     not_included = backtrack(i + 1, curr, memo)

        #     memo[(i + 1, curr + nums[i])] = included
        #     memo[(i + 1, curr)] = not_included

        #     return included or not_included


        # return backtrack(0, 0, {})
        dp = [False] * (amount + 1)
        dp[0] = True

        for num in nums:
            for c in range(amount, num - 1, -1):  # must go backward!
                dp[c] = dp[c] or dp[c - num]

        return dp[amount]


            
