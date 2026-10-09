class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniques = set(nums)
        longest = 0
        for num in nums:
            if num - 1 in uniques:
                continue

            x = num
            while x in uniques:
                x += 1 

            if x - num > longest:
                longest = x - num

        return longest