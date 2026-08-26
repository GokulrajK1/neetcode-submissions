class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        n = len(nums)
        if total % 2 != 0: return False 
        amount = total // 2
        
        def backtrack(i, curr, memo):

            if (i, curr) in memo:
                return memo[(i, curr)]

            if curr == amount:
                return True

            if curr > amount:
                return False 

            if i == n:
                return False 

            included = backtrack(i + 1, curr + nums[i], memo) 
            not_included = backtrack(i + 1, curr, memo)

            memo[(i + 1, curr + nums[i])] = included
            memo[(i + 1, curr)] = not_included

            return included or not_included


        return backtrack(0, 0, {})

            
