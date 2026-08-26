class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        subset = []
        n = len(nums)

        def backtrack(i):
            nonlocal n, res, subset
            if i == n:
                res.append(subset.copy())
                return 

            subset.append(nums[i])
            backtrack(i + 1)
            subset.pop()
            
            j = i 
            while j < n - 1 and nums[j] == nums[j + 1]:
                j += 1 

            backtrack(j + 1)

        backtrack(0)
        return res 
