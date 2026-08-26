class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        curr = []

        def backtrack(total, i):
            if total == target:
                res.append(curr.copy())
                return

            if total > target:
                return 

            if i == len(nums):
                return 

            curr.append(nums[i])
            backtrack(total + nums[i], i)
            curr.pop()
            backtrack(total, i + 1)


        backtrack(0, 0)
        return res 