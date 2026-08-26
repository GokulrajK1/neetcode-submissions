class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        permutation = []
        seen = set()
        def dfs(seen, permutation):
            if len(permutation) == len(nums):
                res.append(permutation.copy())
                return 
            for i in range(len(nums)):
                if nums[i] in seen:
                    continue 
                permutation.append(nums[i])
                seen.add(nums[i])
                dfs(seen, permutation)
                permutation.pop()
                seen.remove(nums[i])

        dfs(seen, permutation)
        return res