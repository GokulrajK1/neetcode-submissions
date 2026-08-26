class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        n = len(nums)
        def backtrack(i):
            nonlocal n
            if i == n:
                res.append(subset.copy())
                return 

            subset.append(nums[i])
            backtrack(i + 1)
            subset.pop()
            backtrack(i + 1)

        backtrack(0)

        return res