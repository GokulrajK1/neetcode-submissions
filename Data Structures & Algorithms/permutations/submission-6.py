class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        curr = []
        seen = set()

        def backtrack(i):
            if i == len(nums):
                res.append(curr.copy())
                return 

            for j in range(len(nums)):
                if nums[j] not in seen:
                    curr.append(nums[j])
                    seen.add(nums[j])
                    backtrack(i + 1)
                    curr.pop()
                    seen.discard(nums[j])

        backtrack(0)

        return res 
