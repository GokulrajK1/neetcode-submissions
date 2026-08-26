class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        combination = []
        def backtrack(nums, total):
     
            if total > target:
                return False 
            if total == target:
                res.append(combination.copy())
                return True

            for i, num in enumerate(nums):
                total += num
                combination.append(num)
                if backtrack(nums[i:], total):
                    total -= num
                    combination.pop()
                else:
                    total -= num
                    combination.pop()

            return False

        backtrack(nums, 0)
        return res

        

                
