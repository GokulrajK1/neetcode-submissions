class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        color_counts = {0 : 0, 1 : 0, 2 : 0}
        for num in nums:
            color_counts[num] = color_counts[num] + 1 
        
        k = 0 
        for i in range(3):
            for j in range(color_counts[i]):
                nums[k] = i 
                k += 1 
        
            
            

        