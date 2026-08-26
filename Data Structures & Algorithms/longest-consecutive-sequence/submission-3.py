class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        starts = set()
        max_length = 0
        nums_set = set(nums)
        for num in nums:
            if num - 1 in starts:
                continue
            starts.add(num)
            i = num
            length = 0
            while i in nums_set:
                length += 1 
                i += 1

            max_length = max(max_length, length)

        return max_length
            

        