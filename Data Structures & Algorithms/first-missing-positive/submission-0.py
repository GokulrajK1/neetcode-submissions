class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        uniques = set(nums)
        n = 1 
        while n in uniques:
            n += 1 

        return n 
