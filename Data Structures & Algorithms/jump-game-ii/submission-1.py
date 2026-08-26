class Solution:
    def jump(self, nums: List[int]) -> int:
        l, r = 0, 0 
        count = 0
        while r < len(nums) - 1:
            max_jump = r 
            for i in range(l, r + 1):

                max_jump = max(max_jump, min(i + nums[i], len(nums) - 1))

            l = r 
            r = max_jump 
            count += 1

        return count 