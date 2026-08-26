class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # right = len(nums) - 1
        # for left in range(right, -1, -1):
        #     if nums[left] >= right - left:
        #         right = left 

        # return right == 0

        l, r = 0, 0
  
        while l <= r and r < len(nums) - 1:
            max_jump = r 
            for i in range(l, r + 1):
                max_jump = max(max_jump, nums[i] + i)

            l = r + 1
            r = max_jump


        return r >= len(nums) - 1
        
