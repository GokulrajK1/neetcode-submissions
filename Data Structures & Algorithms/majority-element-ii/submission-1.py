class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        size = len(nums) // 3 
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1 
        result = []
        for num, count in counts.items():
            if count > size:
                result.append(num)

        return result