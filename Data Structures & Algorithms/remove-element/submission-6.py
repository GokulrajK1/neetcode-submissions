class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        j = len(nums) - 1 
        while i <= j:
            if nums[i] != val:
                i += 1 
            else:
                while nums[j] == val and j >= i:
                    j -= 1 
                if i > j:
                    break
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                i += 1 

        return i


