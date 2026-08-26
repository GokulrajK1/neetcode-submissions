class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement = {}
        for i, num in enumerate(nums):
            if num in complement:
                return [complement[num], i]
            complement[target - num] = i 
        