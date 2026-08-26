class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        r = 0
        for i in range(n):
            if i > r:
                return False 
            r = max(r, i + nums[i])
        return True 
