class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        path = []
        res = []

        def backtrack(i, path):
            if i == len(nums):

                res.append(path.copy())
                return 

            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()
            j = i + 1 
            while j < len(nums) and nums[j] == nums[j - 1]:
                j += 1 
            backtrack(j, path)

        backtrack(0, path)
        return res