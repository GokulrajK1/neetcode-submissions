class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(lo, hi, nums):
            while lo < hi:
                temp = nums[hi]
                nums[hi] = nums[lo]
                nums[lo] = temp 
                lo += 1 
                hi -= 1 
        rotations = k % len(nums)
        reverse(0, len(nums) - 1, nums)
        reverse(0, rotations - 1, nums)
        reverse(rotations, len(nums) - 1, nums)

        

        