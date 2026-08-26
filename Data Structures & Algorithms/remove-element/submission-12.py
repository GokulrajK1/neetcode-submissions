class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0 
        j = len(nums) - 1
        while i < j:
            if nums[j] == val:
                j -= 1 
                continue 
            if nums[i] != val:
                i += 1 
                continue 
            temp = nums[j]
            nums[j] = nums[i]
            nums[i] = temp 

        if i == 0 and j == 0:
            return 0
        
        return i + 1