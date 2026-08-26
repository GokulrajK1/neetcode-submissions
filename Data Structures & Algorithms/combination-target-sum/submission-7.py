class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        curr = []
        n = len(nums)

        def backtrack(i, amount):
            nonlocal n
            if amount == 0:
                res.append(curr.copy())
                return 

            if amount < 0:
                return 
            
            if i == n:
                return 

            curr.append(nums[i])
            backtrack(i, amount - nums[i])
            curr.pop()
            backtrack(i + 1, amount)

        backtrack(0, target)

        return res 