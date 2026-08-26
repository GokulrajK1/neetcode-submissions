class Solution:
    def canJump(self, nums: List[int]) -> bool:
        right = len(nums) - 1
        for left in range(right, -1, -1):
            if nums[left] >= right - left:
                right = left 

        return right == 0
        
