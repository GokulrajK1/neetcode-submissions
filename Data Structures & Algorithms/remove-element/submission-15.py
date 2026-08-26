class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        j = len(nums) - 1
        count = 0
        while i <= j: 
            if nums[i] != val:
                i += 1 
                count += 1 
                continue 
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp
            j -= 1 

        return count
        
        