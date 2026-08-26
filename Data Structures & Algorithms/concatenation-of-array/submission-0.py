class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums2 = nums.copy()
        for num in nums:
            nums2.append(num)

        return nums2