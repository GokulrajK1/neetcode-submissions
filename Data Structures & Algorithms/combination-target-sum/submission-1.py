class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        combination = []
        def backtrack(nums, total):
            if total > target:
                return  
            if total == target:
                res.append(combination.copy())
                return

            for i, num in enumerate(nums):
                total += num
                combination.append(num)
                backtrack(nums[i:], total) 
                total -= num
                combination.pop()

        backtrack(nums, 0)
        return res

        

                
