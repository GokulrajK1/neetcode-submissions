class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairs = {}
        for i, num in enumerate(nums):
            if num in pairs:
                if i > pairs[num]:
                    return [pairs[num], i]
                return [i, pairs[num]]
            else:
                pairs[target - num] = i
