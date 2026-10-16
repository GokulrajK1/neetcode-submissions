class Solution:
    def canJump(self, nums: List[int]) -> bool:
        l, r = 0, 0
        while l <= r and r < len(nums) - 1:
            max_jump = r
            for i in range(l, r + 1):
                max_jump = max(max_jump, i + nums[i])

            l = r + 1 
            r = max_jump 

        return r >= len(nums) - 1

            