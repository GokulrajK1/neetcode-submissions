class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1: return True

        pos = n - 1
        for i in range(n - 2, -1, -1):
            if pos - i <= nums[i]:
                pos = i 
            
        return pos == 0
