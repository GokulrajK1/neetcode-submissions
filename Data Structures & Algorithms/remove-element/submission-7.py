class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        j = len(nums) 
        while i < j:
            if nums[i] != val:
                i += 1 
            else:
                j -= 1
                nums[i] = nums[j]

        return i


