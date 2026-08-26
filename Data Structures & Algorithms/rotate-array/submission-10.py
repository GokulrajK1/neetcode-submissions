class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n

        i = 0 
        j = n - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1 
        
        i1 = 0 
        j1 = k - 1

        while i1 < j1:
            nums[i1], nums[j1] = nums[j1], nums[i1]
            i1 += 1
            j1 -= 1 

        i2 = k 
        j2 = n - 1

        while i2 < j2:
            nums[i2], nums[j2] = nums[j2], nums[i2]
            i2 += 1
            j2 -= 1 


        