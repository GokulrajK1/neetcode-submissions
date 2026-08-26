class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        sizes = {}
        for num in nums:
            size_num = sizes.get(num, 0) 
            size_num += 1 
            if size_num > len(nums) // 2:
                return num 
            sizes[num] = size_num