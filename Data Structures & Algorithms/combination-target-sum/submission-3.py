class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        curr = []

        def backtrack(i, total):

            if total > target:
                return 

            if total == target:
                res.append(curr.copy())
                return

            if i == len(nums):
                return 

            curr.append(nums[i])

            print(curr)

            backtrack(i, total + nums[i])

            curr.pop()

            backtrack(i + 1, total)

        backtrack(0, 0)
        return res

            
                



            