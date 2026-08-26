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

            for j in range(i, len(nums)):
                curr.append(nums[j])
                backtrack(total + nums[j], j)
                curr.pop()

        backtrack(0, 0)
        return res 