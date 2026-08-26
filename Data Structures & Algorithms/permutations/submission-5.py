class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        seen = set()
        n = len(nums)

        def backtrack():
            if len(curr) == n:
                res.append(curr.copy())
                return 

            for i in range(len(nums)):
                if nums[i] in seen:
                    continue 
                curr.append(nums[i])
                seen.add(nums[i])
                backtrack()
                curr.pop()
                seen.remove(nums[i])

        backtrack()
        return res