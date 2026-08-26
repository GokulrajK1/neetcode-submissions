class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        rotations = k % n 
        def reverse(i, j, nums):
            while i < j:
                temp = nums[j]
                nums[j] = nums[i]
                nums[i] = temp 
                i += 1
                j -= 1
            
        reverse(0, n - 1, nums)
        reverse(0, rotations - 1, nums)
        reverse(rotations, n - 1, nums)
    
        