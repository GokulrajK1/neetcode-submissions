class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        n = len(nums)
        nums.sort()

        def backtrack(i):
    
            if i == n:
                res.append(subset.copy())
                return  

            subset.append(nums[i])
            backtrack(i + 1)
            subset.pop()
            j = i + 1 
            while j < n and nums[j] == nums[j - 1]:
                j += 1 

            backtrack(j)

        backtrack(0)
        return res 