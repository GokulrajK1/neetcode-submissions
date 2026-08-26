class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniques = set(nums)
        max_length = 0 
        for num in nums:
            x = num + 1
            while x in uniques:
                x += 1
            length = x - num 
            if length > max_length:
                max_length = length 

        return max_length
            