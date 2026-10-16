class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        picked = [False] * len(nums)

        res = []
        curr = []

        nums.sort()

        def backtrack(i):
            if i == len(nums):
                res.append(curr.copy())
                return 

            for j in range(len(nums)):
                if j > 0 and nums[j] == nums[j - 1] and not picked[j - 1]:
                    continue 

                if not picked[j]:
                    curr.append(nums[j])
                    picked[j] = True 
                    backtrack(i + 1)
                    curr.pop()
                    picked[j] = False 

        backtrack(0)

        return res