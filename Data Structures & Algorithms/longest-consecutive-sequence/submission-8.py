class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = set(nums)
        maxlength = 0
        for num in nums:
            if num - 1 in n:
                continue 
            length = 1 
            x = num
            while x + 1 in n:
                length += 1
                x += 1 
            maxlength = max(maxlength, length)

        return maxlength
            
