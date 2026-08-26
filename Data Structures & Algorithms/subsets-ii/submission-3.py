class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []
        curr = []

        def backtrack(i):
            if i == len(nums):
                res.append(curr.copy())
                return 

            curr.append(nums[i])
            backtrack(i + 1)
            curr.pop()

            j = i + 1
            while j < len(nums) and nums[j] == nums[j - 1]:
                j += 1

            backtrack(j)

        backtrack(0)
        return res