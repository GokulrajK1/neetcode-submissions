class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        curr = []

        def backtrack(i, t):

            if t > target: return 

            if i == len(nums) and t < target: return 

            if i == len(nums) and t == target:
                res.append(curr.copy())
                return 

            curr.append(nums[i])
            t += nums[i]
            backtrack(i, t)
            
            curr.pop()
            t -= nums[i]
            backtrack(i + 1, t)

        backtrack(0, 0)

        return res 